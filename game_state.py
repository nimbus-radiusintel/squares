from square import Square
import random
from maze import get_maze_squares
import pygame
import math

WHITE = (255,255,255)
BLUE = (50,50,200)
RED = (255, 0, 0)
GREEN = (40, 200, 40)

WIDTH = 300
HEIGHT = 300

class GameState:
    def __init__(self):
        self.maze_squares = get_maze_squares()
        self.maze_map = make_maze_map(self.maze_squares)
        print self.maze_map
        self.player = Square(start = [50,50], color=BLUE)
        self.enemies = []
        self.lasers = []
        for i in range(10):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            enemy = Square(start = (x,y), color=RED)
            self.enemies.append(enemy)

    def update(self, control_state):
        self.player.velocity = control_state.get_player_velocity()
        if control_state.firing:
            self.make_new_laser()
        self.player.update_position(self.maze_map)
        for laser in self.lasers:
            laser.update_position(self.maze_map)


    def get_squares(self):
        yield self.player
        for enemy in self.enemies:
            yield enemy
        for maze_square in self.maze_squares:
            yield maze_square
        for laser in self.lasers:
            yield laser

    def make_new_laser(self):
        laser_pos = [0,0]
        laser_pos[0] = self.player.pos[0]
        laser_pos[1] = self.player.pos[1]
        difference = sub_vec(pygame.mouse.get_pos(), self.player.pos)
        laser_speed = unit_vec(difference)
        laser = Square(start=laser_pos,velocity=laser_speed,color=RED)
        self.lasers.append(laser)


def make_maze_map(maze_squares):
    maze_map = {}
    for maze_square in maze_squares:
        for i in range(maze_square.size):
            for j in range(maze_square.size):
                x = maze_square.pos[0] + i
                y = maze_square.pos[1] + j
                maze_map[(x,y)] = 1
    return maze_map

def sub_vec(mouse, player):
    result = [0,0]
    result[0] = mouse[0] - player[0]
    result[1] = mouse[1] - player[1]
    return result


def unit_vec(direction):
    length = math.sqrt(direction[0]**2 + direction[1]**2)
    result = [0,0]
    result[0] = (1/length) * direction[0]
    result[1] = (1/length) * direction[1]
    return result