import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = " "
BGCOLOR = LIGHTGREY

TILESIZE = 64
TILEWIDTH = 2560
TILEHEIGHT = 1280
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_06.png'

# Maps
# LEVEL_MAPS = ['House.tmx', 'example.tmx']
LEVEL_MAPS = 'dungeon.tmx'
# player settings
PLAYER_SPEED = 100

PLAYER_WALKING = 1.6

PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'crusader_idle_00000.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 60, 120)
BARREL_OFFSET = vec(30, 10)
PLAYER_HEALTH = 100
PLAYER_SCALE = (180, 120)
PLAYER_WALK = {}
PLAYER_WALK['southeast'] = ['walk/crusader_walk_10000.png', 'walk/crusader_walk_10001.png', 'walk/crusader_walk_10002.png',
                             'walk/crusader_walk_10003.png', 'walk/crusader_walk_10004.png', 'walk/crusader_walk_10005.png',
                             'walk/crusader_walk_10006.png', 'walk/crusader_walk_10007.png', 'walk/crusader_walk_10008.png',
                             'walk/crusader_walk_10009.png', 'walk/crusader_walk_10010.png', 'walk/crusader_walk_10011.png',
                             'walk/crusader_walk_10012.png', 'walk/crusader_walk_10013.png', 'walk/crusader_walk_10014.png']
PLAYER_WALK['northeast'] = ['walk/crusader_walk_30000.png', 'walk/crusader_walk_30001.png', 'walk/crusader_walk_30002.png',
                             'walk/crusader_walk_30003.png', 'walk/crusader_walk_30004.png', 'walk/crusader_walk_30005.png',
                             'walk/crusader_walk_30006.png', 'walk/crusader_walk_30007.png', 'walk/crusader_walk_30008.png',
                             'walk/crusader_walk_30009.png', 'walk/crusader_walk_30010.png', 'walk/crusader_walk_30011.png',
                             'walk/crusader_walk_30012.png', 'walk/crusader_walk_30013.png', 'walk/crusader_walk_30014.png']
PLAYER_WALK['southwest'] = ['walk/crusader_walk_70000.png', 'walk/crusader_walk_70001.png', 'walk/crusader_walk_70002.png',
                             'walk/crusader_walk_70003.png', 'walk/crusader_walk_70004.png', 'walk/crusader_walk_70005.png',
                             'walk/crusader_walk_70006.png', 'walk/crusader_walk_70007.png', 'walk/crusader_walk_70008.png',
                             'walk/crusader_walk_70009.png', 'walk/crusader_walk_70010.png', 'walk/crusader_walk_70011.png',
                             'walk/crusader_walk_70012.png', 'walk/crusader_walk_70013.png', 'walk/crusader_walk_70014.png']
PLAYER_WALK['northwest'] = ['walk/crusader_walk_50000.png', 'walk/crusader_walk_50001.png', 'walk/crusader_walk_50002.png',
                             'walk/crusader_walk_50003.png', 'walk/crusader_walk_50004.png', 'walk/crusader_walk_50005.png',
                             'walk/crusader_walk_50006.png', 'walk/crusader_walk_50007.png', 'walk/crusader_walk_50008.png',
                             'walk/crusader_walk_50009.png', 'walk/crusader_walk_50010.png', 'walk/crusader_walk_50011.png',
                             'walk/crusader_walk_50012.png', 'walk/crusader_walk_50013.png', 'walk/crusader_walk_50014.png']
PLAYER_WALK['east'] = ['walk/crusader_walk_20000.png', 'walk/crusader_walk_20001.png', 'walk/crusader_walk_20002.png',
                             'walk/crusader_walk_20003.png', 'walk/crusader_walk_20004.png', 'walk/crusader_walk_20005.png',
                             'walk/crusader_walk_20006.png', 'walk/crusader_walk_20007.png', 'walk/crusader_walk_20008.png',
                             'walk/crusader_walk_20009.png', 'walk/crusader_walk_20010.png', 'walk/crusader_walk_20011.png',
                             'walk/crusader_walk_20012.png', 'walk/crusader_walk_20013.png', 'walk/crusader_walk_20014.png']
PLAYER_WALK['north'] = ['walk/crusader_walk_40000.png', 'walk/crusader_walk_40001.png', 'walk/crusader_walk_40002.png',
                             'walk/crusader_walk_40003.png', 'walk/crusader_walk_40004.png', 'walk/crusader_walk_40005.png',
                             'walk/crusader_walk_40006.png', 'walk/crusader_walk_40007.png', 'walk/crusader_walk_40008.png',
                             'walk/crusader_walk_40009.png', 'walk/crusader_walk_40010.png', 'walk/crusader_walk_40011.png',
                             'walk/crusader_walk_40012.png', 'walk/crusader_walk_40013.png', 'walk/crusader_walk_40014.png']
PLAYER_WALK['west'] = ['walk/crusader_walk_60000.png', 'walk/crusader_walk_60001.png', 'walk/crusader_walk_60002.png',
                             'walk/crusader_walk_60003.png', 'walk/crusader_walk_60004.png', 'walk/crusader_walk_60005.png',
                             'walk/crusader_walk_60006.png', 'walk/crusader_walk_60007.png', 'walk/crusader_walk_60008.png',
                             'walk/crusader_walk_60009.png', 'walk/crusader_walk_60010.png', 'walk/crusader_walk_60011.png',
                             'walk/crusader_walk_60012.png', 'walk/crusader_walk_60013.png', 'walk/crusader_walk_60014.png']
PLAYER_WALK['south'] = ['walk/crusader_walk_00000.png', 'walk/crusader_walk_00001.png', 'walk/crusader_walk_00002.png',
                             'walk/crusader_walk_00003.png', 'walk/crusader_walk_00004.png', 'walk/crusader_walk_00005.png',
                             'walk/crusader_walk_00006.png', 'walk/crusader_walk_00007.png', 'walk/crusader_walk_00008.png',
                             'walk/crusader_walk_00009.png', 'walk/crusader_walk_00010.png', 'walk/crusader_walk_00011.png',
                             'walk/crusader_walk_00012.png', 'walk/crusader_walk_00013.png', 'walk/crusader_walk_00014.png']

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,                                  
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12}


# mobs settings
MOB_IMG = 'zoimbie1_hold.png'
MOB_SPLAT = 'splat.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]

# Layers
WALL_LAYER = 3
PLAYER_LAYER = 2
BELOW_PLAYER = 1
GROUND_LAYER = 0
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Item Properties
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_ITEM_SIZE = 45
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/pain_8.wav', 'pain/pain_9.wav', 'pain/pain_10.wav', 'pain/pain_11.wav']
ZOMBIE_MOAN_SOUNDS = ['zombie/brains2.wav', 'zombie/brains3.wav', 'zombie/zombie-roar-1.wav',
                      'zombie/zombie-roar-2.wav', 'zombie/zombie-roar-3.wav', 'zombie/zombie-roar-5.wav',
                      'zombie/zombie-roar-6.wav', 'zombie/zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['special/splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['weapons/pistol.wav'],
                 'shotgun': ['weapons/shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}


