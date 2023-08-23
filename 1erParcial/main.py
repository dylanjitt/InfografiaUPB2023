from typing import Optional, Tuple
import arcade
import random
from gameObjects import Circle, Paddle

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
TITLE="Pong xd"

#Para modificar el limite de goles de la partida!
WINNER_LIMIT=1


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

P1_x=6
P1_Y=(SCREEN_HEIGHT/2)-50
P2_x=SCREEN_WIDTH-36
P2_Y=(SCREEN_HEIGHT/2)-50

class PongWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_speed_default=5
        self.ball_speed=self.ball_speed_default
        self.ball=Circle(SCREEN_WIDTH/2,SCREEN_HEIGHT/4,20,self.ball_speed,arcade.color.PASTEL_YELLOW)
        self.pad_speed=10

        self.color1=get_random_color()
        self.color2=get_random_color()

        self.p1=Paddle(P1_x,P1_Y,self.color1,SCREEN_HEIGHT,True)
        self.p2=Paddle(P2_x,P2_Y,self.color2,SCREEN_HEIGHT,False)

        self.points_P1=arcade.Text(str(self.p1.puntos),SCREEN_WIDTH*(1/4),50,self.color1,30,10,"left","arial",True,False,"left","baseline",False)
        self.points_P2=arcade.Text(str(self.p2.puntos),SCREEN_WIDTH*(3/4),50,self.color2,30,10,"left","arial",True,False,"left","baseline",False)

        self.moving=False
        self.START=arcade.Text("Presiona SPACE para comenzar",SCREEN_WIDTH*2/5,SCREEN_HEIGHT*(2/3),arcade.color.WHITE,40,10,"center","arial",True,False,"center","baseline",False)
        self.textStart=True

        self.PAUSE=arcade.Text("PAUSA",SCREEN_WIDTH*(1.2/3),SCREEN_HEIGHT/2,arcade.color.WHITE,40,10,"center","arial",True,False,"center","baseline",False)

        self.gameOver=False

        self.ganador=arcade.Text("Ganador:",SCREEN_WIDTH*(1/4),SCREEN_HEIGHT/2,arcade.color.WHITE,40,10,"center","arial",True,False,"center","baseline",False)
        self.g1=arcade.Text("J1:",SCREEN_WIDTH*(2.5/4),SCREEN_HEIGHT/2,self.color1,40,10,"center","arial",True,False,"center","baseline",False)
        self.g2=arcade.Text("J2:",SCREEN_WIDTH*(2.5/4),SCREEN_HEIGHT/2,self.color2,40,10,"center","arial",True,False,"center","baseline",False)
        self.gracias=arcade.Text("Gracias por jugar!",SCREEN_WIDTH*(2/4),SCREEN_HEIGHT/3,arcade.color.WHITE,30,600,"center","arial",True,False,"center","baseline",False)
        self.music=arcade.load_sound("1erParcial/faceToFace8Bit.mp3")
        self.music.play()

    #def play(self):
        


    def on_draw(self):
        arcade.start_render()
        if self.gameOver==False:
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
        
        if self.p1.puntos==WINNER_LIMIT or self.p2.puntos==WINNER_LIMIT:
            self.gameOver=True
            #self.music.stop()
            self.ganador.draw()
            if self.p1.puntos==WINNER_LIMIT:
                self.g1.draw()
            if self.p2.puntos==WINNER_LIMIT:
                self.g2.draw()
            self.gracias.draw()

    
    def on_update(self, delta_time: float):
        if self.gameOver==False:
            if self.moving==True:
                self.ball.update(delta_time)  
                self.p1.update(delta_time)
                self.p2.update(delta_time)
        #if self.p1.puntos == WINNER_LIMIT or self.p2.puntos == WINNER_LIMIT:
            #self.gameOver = True
            #self.music.stop()
        

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
            self.ball.speed_x=self.ball_speed_default
            self.ball.speed_y=self.ball_speed_default

            print("gol der")

        #GOL PLAYER IZQ
        if self.ball.x >= SCREEN_WIDTH - self.ball.r:
            self.ball.x=SCREEN_WIDTH/2
            self.ball.y=SCREEN_HEIGHT/2
            self.p1.puntos+=1
            self.ball.speed_x=self.ball_speed_default
            self.ball.speed_y=self.ball_speed_default 
        
            print("gol izq")
        #implementar colisiones con paleta aqui
        self.p1.colissionCircle(self.ball,get_random_color)
        self.p2.colissionCircle(self.ball,get_random_color)

        self.points_P1.text=str(self.p1.puntos)
        self.points_P2.text=str(self.p2.puntos)

    
    def on_key_press(self, symbol: int, modifiers: int):
        
        if self.gameOver==False:
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

            
        