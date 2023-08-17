import arcade
import math


class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 0
        self.angle=0
        self.bullets=[]

    def shoot(self,bullet_speed):
        self.bullets.append((self.center_x,self.center_y,self.angle,bullet_speed))

    def update(self):
        # angle y change_angle expresados grados
        self.angle += self.change_angle
        angle_rad = math.radians(self.angle)

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

        #self.update_bullets(delta_time)

    #def update_bullets(self,delta_time):

class Bullet(arcade.sprite):
    def __init__(self,image,scale,speed,angle,center_x,center_y):
        super.__init__()
