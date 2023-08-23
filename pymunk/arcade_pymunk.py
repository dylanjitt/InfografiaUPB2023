from typing import Optional, Tuple
import math
import arcade
import pyglet
import pymunk

WIDTH=800
HEIGHT=800
TITLE="hello Physics"
class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH,HEIGHT,TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        #crear space de pymunk
        self.space = pymunk.Space()
        self.space.gravity=(0,-981)

        #agregar un body
        body = pymunk.Body(1.0,pymunk.moment_for_box(1.0,(30,30)))
        body.position = (WIDTH/2,HEIGHT/2)
        self.shape = pymunk.Poly.create_box(body,(30,30))
        self.shape.elasticity = 1.0
        self.shape.friction=0.0

        #
        floor_body=pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape=pymunk.Segment()

        #
        self.space.add(body,self.shape)

        self.body_sprite = arcade.SpriteSolidColor(30,30,arcade.color.RED)

    def on_update(self, delta_time: float):
        self.space.step(1/60)
        self.body_sprite.center_x = self.shape.body.position.x
        self.body_sprite.center_y = self.shape.body.position.y
        self.body_sprite.angle = math.degrees(self.shape.body.angle)

    def on_draw(self):
        arcade.start_render()
        self.body_sprite.draw()

if __name__ == "__main__":
    app = App()
    arcade.run()