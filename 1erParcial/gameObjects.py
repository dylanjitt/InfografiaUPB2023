import numpy as np
import arcade
import math

class Circle:
    def __init__(self,x,y,r,speed,color):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.speed_x=speed
        self.speed_y=speed

        self.left=self.x-self.r
        self.right=self.x+self.r

    def draw(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.color)

    def update(self,delta_time:float):
        self.x+=self.speed_x
        self.y+=self.speed_y
        self.left=self.x-self.r
        self.right=self.x+self.r
#-------------------------------------------------------------------------------------------------

class Paddle:
    def __init__(self,x, y,color,limit):#add width
        self.x=x+6
        self.y=y
        self.color=color
        self.speed=0
        self.theta=(math.pi/2)
        self.puntos=0
        self.padHeight=100
        self.padWidth=30
        self.limit=limit

        self.rightUP=[self.x+self.padWidth,self.y+self.padHeight]
        self.rightDown=[self.x+self.padWidth,self.y]
        self.leftDown=[self.x,self.y]
        self.leftUp=[self.x,self.y+self.padHeight]

        self.pad=Polygon([self.leftDown,self.rightDown,self.rightUP,self.leftUp],self.color)
        

    def draw(self):
        self.pad.draw()

    def update(self,delta_time:float):
        
        dy=self.speed*math.sin(self.theta)
        new_y = self.y + dy  #Ayuda a no restringir el movimiento cuando el paddle llega a alguno de los limites
        
        if new_y > 0 and new_y < self.limit - self.padHeight:
            self.y = new_y
            self.rightUP[1] += dy
            self.rightDown[1] += dy
            self.leftUp[1] += dy
            self.leftDown[1] += dy
            self.pad.translate(0, dy)
        
        
    
    def colissionCircle(self,circle: Circle):
        #print(self.rightDown[0], circle.left)

        if self.rightDown[0] >= circle.left and (circle.y>=self.rightDown[1] and circle.y<=self.rightUP[1]):
            #print("choque"+str(circle.left)+", "+str(circle.y))
            circle.speed_x*= -1
            

        if self.leftDown[0] >= circle.right and (circle.y>=self.leftDown[1] and circle.y<=self.leftUp[1]):
            #print("choque"+str(circle.left)+", "+str(circle.y))
            circle.speed_x*= -1
            


class Polygon:
    def __init__(self,vertices,color):
        self.vertices=vertices
        self.color=color

    def draw(self):
        arcade.draw_polygon_outline(self.vertices,self.color,5)

    def translate(self, dx, dy):
        TM = np.array([
            [1, 0, dx], 
            [0, 1, dy], 
            [0, 0, 1]
        ])

        return self.apply_transform(TM)
    
    def apply_transform(self, tr_matrix):
        v_array = np.transpose(np.array(
            [[v[0], v[1], 1] for v in self.vertices]
        ))

        self.vertices = np.transpose(
            np.dot(tr_matrix, v_array)[0:2, :]
        ).tolist()





