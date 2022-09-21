import pygame as pg
import sys
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

    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.wall_sprites = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, LEVEL_MAPS), self)
        self.ground_map = Ground(self, self.map)
        self.wall_map = Walls(self, self.map)
#         self.map_img = self.map.make_map('iso')
#         self.map_rect = self.map_img.get_rect()
#         self.ground_img = self.map.make_map('iso', 'Ground')
#         self.walls_img = self.map.make_map('iso', 'Walls')
#         self.map_img = pg.transform.scale(self.map_img, (TILEWIDTH, TILEHEIGHT))
#         self.ground_rect = self.ground_img.get_rect()
#         self.walls_rect = self.walls_img.get_rect()
#         self.map.create_objects()
#         self.camera = Camera(self.map_rect.width, self.map_rect.height)
        self.camera = Camera(self.ground_map.rect.width, self.ground_map.rect.height)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                origin_x = ((self.map.width / 2))# - self.tilewidth / 2)
                tile_x = tile_object.x / self.map.tileheight
                tile_y = tile_object.y / self.map.tileheight
                
                offset = vec((tile_x - tile_y) * self.map.tilewidth / 2 + origin_x,
                             (tile_x + tile_y) * self.map.tileheight / 2)
                self.player = Player(self, offset.x, offset.y)
            
#                 temp_rect = pg.Rect(offset.x, offset.y, tile_object.width, tile_object.height)
#                 pg.draw.rect(self.game.screen, GREEN, temp_rect, 2)
        
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.events()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
#         print(pg.mouse.get_pos())
#         print(self.player.rect.center)
    
    def draw(self):
        self.screen.fill(BLACK)
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))        
#         self.screen.blit(self.ground_map.image, self.camera.apply_rect(self.ground_map.rect))
#         self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
                print(self.player.rect.center)
        
g = Game()

def main():
    while True:
        g.new()
        g.run()
    
if __name__ == '__main__':
    main()