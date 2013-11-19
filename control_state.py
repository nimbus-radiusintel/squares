import pygame
from pygame.locals import *
import sys

class ControlState:

    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.firing = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)
                if event.key == K_a:
                    self.left = True
                if event.key == K_d:
                    self.right = True
                if event.key == K_w:
                    self.up = True
                if event.key == K_s:
                    self.down = True
            if event.type == KEYUP:
                if event.key == K_a:
                    self.left = False
                if event.key == K_d:
                    self.right = False
                if event.key == K_w:
                    self.up = False
                if event.key == K_s:
                    self.down = False
            if event.type == MOUSEBUTTONDOWN:
                self.firing = True
            if event.type == MOUSEBUTTONUP:
                self.firing = False


    def get_player_velocity(self):
        player_velocity = [0,0]
        if (self.right and not self.left):
            player_velocity[0] = 1
        elif (self.left and not self.right):
            player_velocity[0] = -1
        else:
            player_velocity[0] = 0

        if (self.up and not self.down):
            player_velocity[1]  = -1
        elif (self.down and not self.up):
            player_velocity[1] = 1
        else:
            player_velocity[1] = 0
        return player_velocity
