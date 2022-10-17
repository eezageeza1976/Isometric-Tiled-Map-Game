import pygame as pg
import sys
from ImageLoader import *
from os import path
from tiledmap import *
from settings import *
from camera import *
from sprites import *
vec = pg.math.Vector2

class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 1, 2048)
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_folder = path.join(game_folder, 'maps')
        img_folder = path.join(game_folder, 'img')
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, PLAYER_SCALE)
        self.image_loader = Imageloader()
        

    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player_sprite = pg.sprite.LayeredUpdates()
        self.wall_sprites = pg.sprite.LayeredUpdates()
        self.tree_sprites = pg.sprite.LayeredUpdates()
        self.objects_sprites = pg.sprite.Group()
        self.obs_sprites = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, LEVEL_MAPS), self)
        self.ground_img = self.map.render_ground()
        self.map_rect = self.ground_img.get_rect()
        
        self.camera = Camera(self.map_rect.width, self.map_rect.height)
        self.map.render_by_layer(self.screen, 'Walls')
        
        for tile_object in self.map.tmxdata.objects:
            origin_x = ((self.map.width / 2))
            tile_x = tile_object.x / self.map.tileheight
            tile_y = tile_object.y / self.map.tileheight
            
            offset = vec((tile_x - tile_y) * self.map.tilewidth / 2 + origin_x,
                         (tile_x + tile_y) * self.map.tileheight / 2)
            if tile_object.name == 'player':
                self.player = Player(self, offset.x, offset.y)
                
            if tile_object.name == 'wallBottom':
                Obsticle(self, self.offset_points(tile_object.as_points))
                
    def offset_points(self, points):
        temp_list = []
        for coords in points:
            x_and_y = [pnt for pnt in coords]            
            origin_x = ((self.map.width / 2))
            tile_x = x_and_y[0] / self.map.tileheight
            tile_y = x_and_y[1] / self.map.tileheight
            rect = pg.Rect((tile_x - tile_y) * self.map.tilewidth / 2 + origin_x,
                           (tile_x + tile_y) * self.map.tileheight / 2, 0, 0)
            temp_list.append(rect)
        return temp_list
        
            
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.events()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
        self.obs_sprites.update()
        self.camera.update(self.player)
        
    def draw(self):
#         self.screen.fill(BLACK)
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps())) 
        self.screen.blit(self.ground_img, self.camera.apply_rect(self.map_rect))
#         self.screen.blit(self.player_img, self.camera.apply(self.player))
#         player_pos = self.camera.apply(self.player)
#         pg.draw.circle(self.screen, RED, (player_pos.centerx, player_pos.bottom), 2)
        
        self.wall_sprites.change_layer(self.player, self.player.hit_rect.bottom)
        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                sprite.hit_rect = self.camera.apply_rect(sprite.hit_rect)
                pg.draw.rect(self.screen, BLUE, sprite.hit_rect, 1)
                
            sprite.rect = self.camera.apply_rect(sprite.rect)
#             if not isinstance(sprite, Player):
#                 sprite.set_alpha(100, flags=pg.RLEACCEL)
#             pg.draw.rect(self.screen, RED, sprite.rect, 1)
#         for obs in self.objects_sprites:
#             obs_pos = self.camera.apply(obs)
#             pg.draw.circle(self.screen, RED, (obs_pos.centerx, obs_pos.centery), 2)
        self.wall_sprites.draw(self.screen) 
        for obs in self.obs_sprites:
            temp_pnts = []
            for point in obs.points:
                pnt_rect = self.camera.apply_rect(point)
                pnt = vec(pnt_rect.left, pnt_rect.top)
                temp_pnts.append(pnt)
#             obs.points = temp_pnts
            pg.draw.lines(self.screen, GREEN, True, temp_pnts, 2)
                    
                            
        pg.display.flip()
    
    def quit(self):
        pg.quit()
        sys.exit()
        
    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())
        
g = Game()

def main():
    while True:
        g.new()
        g.run()
    
if __name__ == '__main__':
    main()
