
import arcade
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="holaa"

class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)