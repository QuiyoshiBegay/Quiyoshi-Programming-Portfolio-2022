# game options/settings
TITLE = "JUMP SOULS"
WIDTH = 580
HEIGHT = 820
FPS = 60
FONT_NAME = 'Tsukushi Old Mincho'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 20, 20)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 205)
BGCOLOR = LIGHTBLUE

# game properties
BOOST_POWER = 40
POW_SPAWN_PCT = 12
MOB_FREQ = 3000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 21

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]