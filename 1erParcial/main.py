from typing import Optional, Tuple
import arcade
import pyglet
from gameObjects import Circle, Paddle

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
TITLE="Pong xd"



class PongWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_speed_default=5
        self.ball_speed=self.ball_speed_default
        self.ball=Circle(SCREEN_WIDTH/2,SCREEN_HEIGHT/4,20,self.ball_speed,arcade.color.PASTEL_YELLOW)
        self.pad_speed=10

        self.color1=arcade.color.WHITE
        self.color2=arcade.color.WHITE

        self.p1=Paddle(0,(SCREEN_HEIGHT/2)-50,self.color1,SCREEN_HEIGHT)
        self.p2=Paddle(SCREEN_WIDTH-36,(SCREEN_HEIGHT/2)-50,self.color2,SCREEN_HEIGHT)

        self.points_P1=arcade.Text(str(self.p1.puntos),SCREEN_WIDTH*(1/4),50,self.color1,20,10,"left","arial",True,False,"left","baseline",False)
        self.points_P2=arcade.Text(str(self.p2.puntos),SCREEN_WIDTH*(3/4),50,self.color2,20,10,"left","arial",True,False,"left","baseline",False)

        self.moving=False
        self.START=arcade.Text("Presiona SPACE para comenzar",SCREEN_WIDTH*2/5,SCREEN_HEIGHT*(2/3),arcade.color.WHITE,40,10,"center","arial",True,False,"center","baseline",False)
        self.textStart=True

        self.PAUSE=arcade.Text("PAUSA",SCREEN_WIDTH*(1.2/3),SCREEN_HEIGHT/2,arcade.color.WHITE,40,10,"center","arial",True,False,"center","baseline",False)
        self.winnerLimit=1


    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.p1.draw()
        self.p2.draw()

        self.points_P1.draw()
        self.points_P2.draw()

        if self.textStart:
            self.START.draw()
        if self.moving==False:
            if self.textStart==False:
                self.PAUSE.draw()
    
    def on_update(self, delta_time: float):
        if self.moving==True:
            self.ball.update(delta_time)
            self.p1.update(delta_time)
            self.p2.update(delta_time)
        
        

        #IZQ, DER
        if self.ball.x <= self.ball.r or self.ball.x >= SCREEN_WIDTH - self.ball.r:
            self.ball.speed_x *= -1
        if self.ball.y <= self.ball.r or self.ball.y >= SCREEN_HEIGHT - self.ball.r:
            self.ball.speed_y *= -1
        
        
        #GOL PLAYER DER
        if self.ball.x <= self.ball.r:
            self.ball.x=SCREEN_WIDTH/2
            self.ball.y=SCREEN_HEIGHT/2
            self.p2.puntos+=1
            
            print("gol der")

        #GOL PLAYER IZQ
        if self.ball.x >= SCREEN_WIDTH - self.ball.r:
            self.ball.x=SCREEN_WIDTH/2
            self.ball.y=SCREEN_HEIGHT/2
            self.p1.puntos+=1
           
            print("gol izq")
        #implementar colisiones con paleta aqui
        self.p1.colissionCircle(self.ball)
        self.p2.colissionCircle(self.ball)

        self.points_P1.text=str(self.p1.puntos)
        self.points_P2.text=str(self.p2.puntos)

    
    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol== arcade.key.SPACE:
            if self.moving == True:
                self.moving = False
            else:
                self.moving = True

            if self.textStart== True:
                self.textStart=False

        if symbol == arcade.key.W:
            self.p1.speed=self.pad_speed  
        if symbol == arcade.key.S:
            self.p1.speed=-self.pad_speed
        
        if symbol == arcade.key.UP:
            self.p2.speed=self.pad_speed
        if symbol == arcade.key.DOWN:
            self.p2.speed=-self.pad_speed

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP,arcade.key.DOWN):
            self.p2.speed=0
        if symbol in (arcade.key.W,arcade.key.S):
            self.p1.speed=0

    
if __name__ == "__main__":
    app = PongWindow()
    arcade.run()

            
        