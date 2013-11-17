import pygame
import time
from pygame.locals import *
import random
import math

WHITE = (255,255,255)
BLUE = (50,50,200)
RED = (255, 0, 0)
GREEN = (40, 200, 40)
TILESIZE = 10

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window_offset = [0,0]

    def update(self, game_state):
        self.set_offset(game_state)
        self.screen.fill((0,0,0))
        for square in game_state.get_squares():
            self.draw_square(square)
#        draw_grid(self.screen)
        pygame.display.flip()

    def set_offset(self, game_state):
        player = game_state.player
        center_x = player.pos[0] + player.size / 2
        center_y = player.pos[1] + player.size / 2
        self.window_offset[0] = center_x - WINDOW_WIDTH / 2
        self.window_offset[1] = center_y - WINDOW_HEIGHT / 2

    def draw_square(self, square):
        x, y = square.pos
        x -= self.window_offset[0]
        y -= self.window_offset[1]
        size = square.size
        color = square.color
        pygame.draw.rect(self.screen, color, Rect(x,y, size,size))



def draw_grid(screen, n=None):
    if n is None:
        n = max(width, height) / TILESIZE
    for i in range(n):
        x = i*TILESIZE
        pygame.draw.line(screen, WHITE, (x, 0), (x, height))
    for i in range(n):
        y = i * TILESIZE
        pygame.draw.line(screen, WHITE, (0, y), (width, y))
