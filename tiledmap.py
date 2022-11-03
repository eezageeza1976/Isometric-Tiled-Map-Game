import pygame as pg
import pytmx
from sprites import *
from settings import *
vec = pg.math.Vector2

def collide_hit_rect(player, wall):
    return player.hit_rect.colliderect(wall.rect)

class TiledMap:
    def __init__(self, filename, game):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.tilewidth = tm.tilewidth
        self.tileheight = tm.tileheight
        self.game = game
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        
    def ortho_render(self):
        temp_surface = pg.Surface((self.width, self.height))
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        temp_surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
        return temp_surface

    def make_map(self, map_render):
        if map_render == 'ortho':
            return self.ortho_render()
        if map_render == 'iso':
            return self.isometric_render()
    
    def isometric_render(self):
        temp_surface = pg.Surface((self.width, self.height))
        ti = self.tmxdata.get_tile_image_by_gid
        starting_x = ((self.width / 2) - self.tilewidth / 2)
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)                    
                    offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                                 ((x + y) * self.tileheight / 2) - 370)                    
                    if tile:
                        temp_surface.blit(tile, (offset.x, offset.y))
        return temp_surface
    
    def render_ground(self):
        temp_surface = pg.Surface((self.width, self.height))
        ti = self.tmxdata.get_tile_image_by_gid
        lname = self.tmxdata.get_layer_by_name('Ground')
        starting_x = ((self.width / 2) - self.tilewidth / 2)
        if isinstance(lname, pytmx.TiledTileLayer):
            for x, y, gid in lname:
                tile = ti(gid)
                offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                             ((x + y) * self.tileheight / 2) - 370)                    
                if tile:
                    temp_surface.blit(tile, (offset.x, offset.y))
                    
        lname = self.tmxdata.get_layer_by_name('Walls')
        if isinstance(lname, pytmx.TiledTileLayer):
            for x, y, gid in lname:
                if x == 0 or y == 0:
                    tile = ti(gid)
                    offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                                 ((x + y) * self.tileheight / 2) - 370)
                    if tile:
                        temp_surface.blit(tile, (offset.x, offset.y))
                    
        return temp_surface
                            
    def render_by_layer(self, surface, layer_name):
        ti = self.tmxdata.get_tile_image_by_gid
        lname = self.tmxdata.get_layer_by_name(layer_name)
        starting_x = ((self.width / 2) - self.tilewidth / 2)
        
        if isinstance(lname, pytmx.TiledTileLayer):
            for x, y, gid in lname:
                if y != 0:
                    if x != 0:
                        if gid != 0:
                            tile = ti(gid)                    
                            offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                                         ((x + y) * self.tileheight / 2) - 370)
                            if tile:
                                Wall(self.game, offset.x, offset.y, tile)
                            
    def render(self, surface, player_y):
        ti = self.tmxdata.get_tile_image_by_gid
        starting_x = ((self.width / 2) - self.tilewidth / 2)
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)                    
                    offset = vec(((x - y) * self.tilewidth / 2) + starting_x,
                                 ((x + y) * self.tileheight / 2) - 370)                    
                    if tile:
                        if player_y < offset.y:
                            surface.blit(self.game.player.image,
                                         self.game.camera.apply(self.game.player))
#                             surface.blit(tile, (offset.x, offset.y))
                        else:
                            surface.blit(tile, (offset.x, offset.y))

