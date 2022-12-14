import pygame as pg
import pytmx
from settings import *

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        
        #  limit scrolling map
        x = min(0, x)  #  left
        y = min(0, y)  #  top
        x = max(-(self.width - WIDTH), x)  #  right
        y = max(-(self.height - HEIGHT), y)  #  bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
        
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)