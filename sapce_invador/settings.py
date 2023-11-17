import pygame
import random
from entitys import Button as bt
from entitys import Star

# Screen settings
WIDTH_SCREEN = 700
HEIGHT_SCREEN = 600
SCREEN = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
SCREEN_RECT = SCREEN.get_rect()
SCREEN_FILL = "black"

# Player settings
SHIP_IMAGE = pygame.image.load("ship.bmp")
SHIP_SIZE = (WIDTH_SCREEN // 15, HEIGHT_SCREEN // 15)
PLAYER_POS = pygame.Vector2(SCREEN.get_width() // 2, SCREEN.get_height() // 10 * 9)
PLAYER_LIFE = 3
PLAYER_SPEED = 5
NUM_OF_PLAYER_BULLET = 4

# Enemy settings
INVADER_IMAGE = pygame.image.load("alien.bmp")
INVADER_SIZE = (WIDTH_SCREEN // 15, HEIGHT_SCREEN // 15)
NUM_OF_ENEMY_BULLET = 0.01
ENEMY_SPEED = 3
ENEMY_LIFE = 1
ROW_OF_ENTMEIS = 2
PLAYER_IMAGE = pygame.transform.scale(SHIP_IMAGE, SHIP_SIZE)
ENEMY_IMAGE = pygame.transform.scale(INVADER_IMAGE, SHIP_SIZE)

# Bullet settings
BULLET1_IMAGE = pygame.image.load("bullet.png").convert_alpha()
BULLET_SIZE = (16,16)
BULLET_IMAGE = pygame.transform.scale(BULLET1_IMAGE, BULLET_SIZE)
BULLET_SPEED = 5

# Game settings
LEVEL = 1
FPS = 60
CLOCK = pygame.time.Clock()
WIDTH = 50
HEIGHT = 70
IF_START = False
RUN = True
LINE_HEIGHT = HEIGHT_SCREEN - 25

# start button
DISPLAY_START = True
START_IMG = pygame.image.load('start.png').convert_alpha()
START_BUTTON = bt(350, 300, START_IMG, 0.8)

# Star settings and create
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x = 1
y = 1
yspeed = 5
stars = []
for i in range(100):
    x = random.randint(1, WIDTH_SCREEN - 1)
    y = random.randint(1, HEIGHT_SCREEN - 1)
    stars.append(Star(x, y, yspeed))


