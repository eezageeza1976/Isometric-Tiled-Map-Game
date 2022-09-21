import pygame as pg
import pytmx
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        
    def update(self):
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        
    
    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel = self.xy_to_iso(vec(-PLAYER_SPEED, 0))
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel = self.xy_to_iso(vec(PLAYER_SPEED, 0))
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = self.xy_to_iso(vec(0, -PLAYER_SPEED))
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = self.xy_to_iso(vec(0, PLAYER_SPEED))
            
    def xy_to_iso(self, v):
        return vec((v.x - v.y), (v.x + v.y) / 2)      

def isometric_render(layer, tiled_map):
    temp_surface = pg.Surface((tiled_map.width, tiled_map.height))
    current_layer = tiled_map.tmxdata.get_layer_by_name(layer)
    ti = tiled_map.tmxdata.get_tile_image_by_gid           
    if isinstance(current_layer, pytmx.TiledTileLayer):
        for x, y, gid in current_layer:
            if gid != 0:
                starting_x = ((tiled_map.width / 2) - tiled_map.tilewidth / 2)
                offset = vec(((x - y) * tiled_map.tilewidth / 2) + starting_x,
                             ((x + y) * tiled_map.tileheight / 2) - 370)
                tile = ti(gid)
                
                if tile:
                    temp_surface.blit(tile, (offset.x, offset.y))
    return temp_surface
                            
class Ground(pg.sprite.Sprite):
    def __init__(self, game, tiled_map):
        self._layer = GROUND_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = isometric_render('Ground', tiled_map)
        self.rect = self.image.get_rect()
            
class Walls(pg.sprite.Sprite):
    def __init__(self, game, tiled_map):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites, game.wall_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = isometric_render('Walls', tiled_map)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
class obsticle(pg.sprite.Sprite):
    def __init__(self, game, tiled_map):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = isometric_render('Obsticles', tiled_map)
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)