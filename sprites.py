import pygame as pg
import pytmx
from tiledmap import *
from settings import *
from camera import *
from collision import collide_with_walls
vec = pg.math.Vector2



class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.player_sprite, game.wall_sprites     
#         self.image = game.player_img
        self.game = game
        self.load_images()
        self.image = self.walk_e_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._layer = self.rect.bottom
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        pg.sprite.Sprite.__init__(self, self.groups)
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.working_frames = self.walk_e_imgs
        self.player_speed = PLAYER_WALKING
        self.last_update = 0
        self.current_frame = 0
        self.walking = False
    
    def load_images(self):
        self.walk_se_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'southeast', True)
        self.walk_ne_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'northeast', True)
        self.walk_sw_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'southwest', True)
        self.walk_nw_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'northwest', True)
        self.walk_e_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'east', True)
        self.walk_n_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'north', True)
        self.walk_w_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'west', True)
        self.walk_s_imgs = self.game.image_loader.get_image(PLAYER_WALK, 'south', True)
    
    def update(self):
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        # collide_with_walls(self.game.obs_sprites, self, 'x')
        # collide(self.game.obs_sprites, (self.game.player.rect.centerx, self.game.player.rect.centery))
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self.game.obs_sprites, self, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self.game.obs_sprites, self, 'y')
        self.rect.center = self.hit_rect.center
        
    
    def get_keys(self):
        self.animate()
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.walking = True
            self.working_frames = self.walk_nw_imgs
            self.vel = self.xy_to_iso(vec(-PLAYER_SPEED, 0))
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.walking = True
            self.working_frames = self.walk_se_imgs
            self.vel = self.xy_to_iso(vec(PLAYER_SPEED, 0))
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.walking = True
            self.working_frames = self.walk_ne_imgs
            self.vel = self.xy_to_iso(vec(0, -PLAYER_SPEED))
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.walking = True
            self.working_frames = self.walk_sw_imgs
            self.vel = self.xy_to_iso(vec(0, PLAYER_SPEED))
            
    def xy_to_iso(self, v):
        return vec((v.x - v.y), (v.x + v.y) / 2)      
                           
    def animate(self):
        now = pg.time.get_ticks()
            
        if now - self.last_update > 30 * self.game.dt:
            if not self.walking:
                self.current_frame = 0
                self.image = self.working_frames[self.current_frame]
            elif self.walking:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.working_frames)
                self.image = self.working_frames[self.current_frame]
                self.walking = False
            
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.wall_sprites        
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos
        self._layer = self.rect.bottom
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

class Tree(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.tree_sprites        
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.rect.bottom - 30
        self.pos = vec(x, y)
        self.rect.topleft = self.pos
        self._layer = self.rect.bottom
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.bottom = self.rect.bottom - 30
        print(self.rect)
        self.rect.topleft = self.pos
        
class Obsticle(pg.sprite.Sprite):
    def __init__(self, game, point_list):
        self.groups = game.obs_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.points = point_list
        self.pos1 = vec(point_list[0][0], point_list[0][1])
        self.pos2 = vec(point_list[1][0], point_list[1][1])
        self.pos3 = vec(point_list[2][0], point_list[2][1])
        self.pos4 = vec(point_list[3][0], point_list[3][1])
        
    def update(self):
        self.points[0].topleft = self.pos1
        self.points[1].topleft = self.pos2
        self.points[2].topleft = self.pos3
        self.points[3].topleft = self.pos4

        
        

