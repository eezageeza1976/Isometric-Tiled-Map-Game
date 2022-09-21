import pygame as pg
import pytmx
from settings import *
from sprites import Player
vec = pg.math.Vector2
        
class TiledMap:
    def __init__(self, filename, game):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.tilewidth = tm.tilewidth
        self.tileheight = tm.tileheight
        self.game = game
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        
    def ortho_render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
    
    def render_layers(self, surface, layer):
        ti = self.tmxdata.get_tile_image_by_gid
#         for layer in self.tmxdata.visible_layers:
        print(self.tmxdata.get_layer_by_name(layer))
#             if isinstance(layer, pytmx.TiledTileLayer):
#                 for x, y, gid in layer:
#                     if gid != 0:
#                         starting_x = ((self.width / 2) - self.tilewidth / 2)
#                         offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
#                                      ((x + y) * self.tileheight / 2) - 370)
#                         tile = ti(gid)
#                         
#                         if tile:
#                             surface.blit(tile, (offset.x, offset.y))
                            
    def isometric_render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:            
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if gid != 0:
                        starting_x = ((self.width / 2) - self.tilewidth / 2)
                        offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                                     ((x + y) * self.tileheight / 2) - 370)
                        tile = ti(gid)
                        
                        if tile:
                            surface.blit(tile, (offset.x, offset.y))
    
    def create_objects(self):
        for tile_object in self.tmxdata.objects:
            if tile_object.name == 'player':
                origin_x = ((self.width / 2))# - self.tilewidth / 2)
                tile_x = tile_object.x / self.tileheight
                tile_y = tile_object.y / self.tileheight
                
                offset = vec((tile_x - tile_y) * self.tilewidth / 2 + origin_x,
                             (tile_x + tile_y) * self.tileheight / 2)
                self.game.player = Player(self.game, offset.x, offset.y)
            if tile_object.name == 'wall':
                print(dir(tile_object))
                origin_x = ((self.width / 2))# - self.tilewidth / 2)
                tile_x = tile_object.x / self.tileheight
                tile_y = tile_object.y / self.tileheight
                
                offset = vec((tile_x - tile_y) * self.tilewidth / 2 + origin_x,
                             (tile_x + tile_y) * self.tileheight / 2)
                temp_rect = pg.Rect(offset.x, offset.y, tile_object.width, tile_object.height)
                pg.draw.rect(self.game.screen, GREEN, temp_rect, 2)
    
    def make_map(self, map_render):
        temp_surface = pg.Surface((self.width, self.height))
        if map_render == 'ortho':
            self.ortho_render(temp_surface)
        if map_render == 'iso':
            self.isometric_render(temp_surface)
        return temp_surface
