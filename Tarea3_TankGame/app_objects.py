import numpy as np
import arcade
import math


class Polygon2D:
    def __init__(self, vertices, color, rot_speed=0):
        self.vertices = vertices
        self.color = color
        self.rot_speed = rot_speed

    def translate(self, dx, dy):
        TM = np.array([
            [1, 0, dx], 
            [0, 1, dy], 
            [0, 0, 1]
        ])

        return self.apply_transform(TM)
    
    def rotate(self, theta, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()

        Mt1 = np.array([
            [1, 0, -xc], 
            [0, 1, -yc], 
            [0, 0, 1]
        ])
        Mr = np.array([
            [np.cos(theta), -np.sin(theta), 0], 
            [np.sin(theta), np.cos(theta), 0], 
            [0, 0, 1]
        ])
        Mt2 = np.array([
            [1, 0, xc], 
            [0, 1, yc], 
            [0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Mr, Mt1))
  
        return self.apply_transform(TM)

    def scale(self, sx, sy, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()
        Mt1 = np.array([
            [1, 0, -xc], 
            [0, 1, -yc], 
            [0, 0, 1]
        ])
        Ms = np.array([
            [sx, 0, 0], 
            [0, sy, 0], 
            [0, 0, 1]
        ])
        Mt2 = np.array([
            [1, 0, xc], 
            [0, 1, yc], 
            [0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Ms, Mt1))
  
        return self.apply_transform(TM)

    def apply_transform(self, tr_matrix):
        v_array = np.transpose(np.array(
            [[v[0], v[1], 1] for v in self.vertices]
        ))

        self.vertices = np.transpose(
            np.dot(tr_matrix, v_array)[0:2, :]
        ).tolist()

    def get_center(self):
        return np.mean(np.array(self.vertices), axis=0)

    def draw(self):
        arcade.draw_polygon_outline(self.vertices, self.color, 5)

#Tank 1------------------------------------------------------------
class Tank:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.speed = 0
        self.angular_speed = 0
        self.theta = 0
        self.puntos = 0
        self.vida = 3
        self.body = Polygon2D([(100 + x, y), (x, 50 + y), (x, -50 + y)], color)
        self.left_track = Polygon2D(
            [
                (-40 + x, -30 + y), 
                (60 + x, -30 + y),
                (60 + x, -60 + y),
                (-40 + x, -60 + y), 
            ],
            color
        )
        self.right_track = Polygon2D(
            [
                (-40 + x, 30 + y), 
                (60 + x, 30 + y),
                (60 + x, 60 + y),
                (-40 + x, 60 + y), 
            ],
            color
        )
        self.bullets = []
    
    def shoot(self, bullet_speed):
        self.bullets.append((self.x, self.y, self.theta, bullet_speed))

    def update(self, delta_time: float):
        dtheta = self.angular_speed * delta_time
        dx = self.speed * math.cos(self.theta)
        dy = self.speed * math.sin(self.theta)
        self.theta += dtheta
        self.x += dx
        self.y += dy
        self.body.translate(dx, dy)
        self.left_track.translate(dx, dy)
        self.right_track.translate(dx, dy)
        
        self.body.rotate(dtheta, pivot=(self.x, self.y))
        self.left_track.rotate(dtheta, pivot=(self.x, self.y))
        self.right_track.rotate(dtheta, pivot=(self.x, self.y))

        self.update_bullets(delta_time)

    def update_bullets(self, delta_time):
        for i, (x, y, theta, speed) in enumerate(self.bullets):
            new_x = x + speed * math.cos(theta)
            new_y = y + speed * math.sin(theta)
            self.bullets[i] = (new_x, new_y, theta, speed)

    def draw(self):
        self.body.draw()
        self.left_track.draw()
        self.right_track.draw()
        arcade.draw_point(self.x, self.y, arcade.color.RED, 4)

        for bx, by, theta, speed in self.bullets:
            arcade.draw_point(bx, by, arcade.color.YELLOW, 7)

    def detect_collision(self, target_tank: 'Tank2'):
        for bullet in self.bullets:
            if self.point_inside_polygon((bullet[0], bullet[1]), target_tank.body.vertices):
                target_tank.take_damage()
                self.countDamage()

    def point_inside_polygon(self, point, vertices):
        x, y = point
        n = len(vertices)
        inside = False
        p1x, p1y = vertices[0]
        for i in range(n + 1):
            p2x, p2y = vertices[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def distance_to_bullet(self, bullet):
        bx, by, _, _ = bullet
        return math.sqrt((bx - self.x)**2 + (by - self.y)**2)
    
    def countDamage(self):
        self.puntos+=1
    
    def take_damage(self):
        self.vida-=1
        if self.vida==0:
          arcade.draw_circle_filled(self.x, self.y, 10, arcade.color.RED)


#Tank 2------------------------------------------------------------
class Tank2:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.speed = 0
        self.angular_speed = 0
        self.theta = 0
        self.vida = 3
        self.puntos = 0
        self.body = Polygon2D([(100 + x, y), (x, 50 + y), (x, -50 + y)], color)
        self.left_track = Polygon2D(
            [
                (-40 + x, -30 + y), 
                (60 + x, -30 + y),
                (60 + x, -60 + y),
                (-40 + x, -60 + y), 
            ],
            color
        )
        self.right_track = Polygon2D(
            [
                (-40 + x, 30 + y), 
                (60 + x, 30 + y),
                (60 + x, 60 + y),
                (-40 + x, 60 + y), 
            ],
            color
        )
        self.bullets = []
    
    def shoot(self, bullet_speed):
        self.bullets.append((self.x, self.y, self.theta, bullet_speed))

    def update(self, delta_time: float):
        dtheta = self.angular_speed * delta_time
        dx = self.speed * math.cos(self.theta)
        dy = self.speed * math.sin(self.theta)
        self.theta += dtheta
        self.x += dx
        self.y += dy
        self.body.translate(dx, dy)
        self.left_track.translate(dx, dy)
        self.right_track.translate(dx, dy)
        
        self.body.rotate(dtheta, pivot=(self.x, self.y))
        self.left_track.rotate(dtheta, pivot=(self.x, self.y))
        self.right_track.rotate(dtheta, pivot=(self.x, self.y))

        self.update_bullets(delta_time)

    def update_bullets(self, delta_time):
        for i, (x, y, theta, speed) in enumerate(self.bullets):
            new_x = x + speed * math.cos(theta)
            new_y = y + speed * math.sin(theta)
            self.bullets[i] = (new_x, new_y, theta, speed)

    def draw(self):
        self.body.draw()
        self.left_track.draw()
        self.right_track.draw()
        arcade.draw_point(self.x, self.y, arcade.color.GREEN, 4)

        for bx, by, theta, speed in self.bullets:
            arcade.draw_point(bx, by, arcade.color.BLUE, 7)
    
    def detect_collision(self, target_tank: 'Tank'):
        for bullet in self.bullets:
            if self.point_inside_polygon((bullet[0], bullet[1]), target_tank.body.vertices):
                target_tank.take_damage()
                self.countDamage()

    def point_inside_polygon(self, point, vertices):
        x, y = point
        n = len(vertices)
        inside = False
        p1x, p1y = vertices[0]
        for i in range(n + 1):
            p2x, p2y = vertices[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def distance_to_bullet(self, bullet):
        bx, by, _, _ = bullet
        return math.sqrt((bx - self.x)**2 + (by - self.y)**2)
    
    def countDamage(self):
        self.puntos+=1
    
    def take_damage(self):
        self.vida-=1
        if self.vida==0:
          arcade.draw_circle_filled(self.x, self.y, 10, arcade.color.RED)  

#Enemigo-------------------------------------------------------------
class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.is_alive = True
    
    def detect_collision(self, tank: Tank,tank2: Tank2):
        for bullet in tank.bullets:
            if self.distance_to(bullet) < self.r:
                self.is_alive = False
        for bullet in tank2.bullets:
            if self.distance_to(bullet) < self.r:
                self.is_alive = False
                tank2.countDamage()
    
    def distance_to(self, bullet):
        xb, yb, tb, sb = bullet
        return math.sqrt((xb - self.x)**2 + (yb - self.y)**2)

    def draw(self):
        if self.is_alive:
            arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.RED_DEVIL)