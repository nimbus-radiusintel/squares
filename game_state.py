from square import Square
import random
from maze import get_maze_squares


WHITE = (255,255,255)
BLUE = (50,50,200)
RED = (255, 0, 0)
GREEN = (40, 200, 40)

WIDTH = 300
HEIGHT = 300

class GameState:
    def __init__(self):
        self.maze_squares = get_maze_squares()
        self.player = Square(start = [50,50], color=BLUE)
        self.enemies = []
        for i in range(10):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            enemy = Square(start = (x,y), color=RED)
            self.enemies.append(enemy)

    def update(self, control_state):
        self.player.velocity = control_state.get_player_velocity()
        self.player.update_position()

    def get_squares(self):
        yield self.player
        for enemy in self.enemies:
            yield enemy
        for maze_square in self.maze_squares:
            yield maze_square

