import pygame as pg
from settings import *
from os import path

class Imageloader:
    # utility class for loading and parsing spritesheets
    def __init__(self):
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, 'Mini Crusader Graphics')
        
    def get_image(self, action, direction, scale = True):
        temp_list = []
        for img in action[direction]:
            image = pg.image.load(path.join(self.img_dir, img)).convert_alpha()
            if scale:
                image = pg.transform.scale(image, PLAYER_SCALE)
            temp_list.append(image)
        return temp_list