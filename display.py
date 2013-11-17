import pygame
import time
from pygame.locals import *
import random
import math
size = width, height = 320, 240

WHITE = (255,255,255)
BLUE = (50,50,200)
RED = (255, 0, 0)
GREEN = (40, 200, 40)
TILESIZE = 10

class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((320,240))

    def update(self, game_state):
        self.screen.fill((0,0,0))
        draw_grid(self.screen)
        pygame.display.flip()



def draw_grid(screen, n=None):
    if n is None:
        n = max(width, height) / TILESIZE
    for i in range(n):
        x = i*TILESIZE
        pygame.draw.line(screen, WHITE, (x, 0), (x, height))
    for i in range(n):
        y = i * TILESIZE
        pygame.draw.line(screen, WHITE, (0, y), (width, y))
