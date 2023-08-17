from typing import Optional
import arcade
from arcade import Texture

class Player(arcade.Sprite):
    def __init__(self,image,scale,center_x,center_y):
        super().__init__(image,scale,center_x=center_x,center_y=center_y)
        self.speed=0

    def update(self):
        self.center_x+=self.speed