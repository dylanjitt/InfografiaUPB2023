import arcade
import random
from app_objects import Tank,Tank2, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Tank"

SPEED = 10

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.t1color=get_random_color()
        self.t2color=get_random_color()
        self.tank = Tank(600, 400, self.t1color)
        self.tank2 = Tank2(200, 400, self.t2color)
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT),
                random.randrange(10, 50)
            )
            for _ in range(10)
        ]
        self.points_T1=arcade.Text(str(self.tank.puntos),600,50,self.t1color,20,10,"left","arial",True,False,"left","baseline",False)
        self.points_T2=arcade.Text(str(self.tank2.puntos),200,50,self.t2color,20,10,"left","arial",True,False,"left","baseline",False)

    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.tank.shoot(20)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED
        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = 2
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -2

        if symbol == arcade.key.W:
            self.tank2.speed = SPEED
        if symbol == arcade.key.S:
            self.tank2.speed = -SPEED
        if symbol == arcade.key.A:
            self.tank2.angular_speed = 2
        if symbol == arcade.key.D:
            self.tank2.angular_speed = -2
        if symbol == arcade.key.SPACE:
            self.tank2.shoot(20)          
            
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tank.speed = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tank.angular_speed = 0

        if symbol in (arcade.key.W, arcade.key.S):
            self.tank2.speed = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.tank2.angular_speed = 0

    def on_update(self, delta_time: float):
        self.tank.update(delta_time)
        self.tank2.update(delta_time)

        self.tank.detect_collision(self.tank2)
        self.tank2.detect_collision(self.tank)
        for e in self.enemies:
            e.detect_collision(self.tank,self.tank2)

        self.points_T1.text=str(self.tank.puntos)
        self.points_T2.text=str(self.tank2.puntos)
        
    def on_draw(self):
        arcade.start_render()
        self.tank.draw()
        self.tank2.draw()
        for e in self.enemies:
            e.draw()
        self.points_T1.draw()
        self.points_T2.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()