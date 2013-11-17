import time
from display import Display
from game_state import GameState
from control_state import ControlState


class Game(object):

    def __init__(self):
        self.display = Display()
        self.game_state = GameState()
        self.control_state = ControlState()

    def run(self):
        while True:
            self.control_state.update()
            self.game_state.update(self.control_state)
            self.display.update(self.game_state)
            print 'running'
            time.sleep(1)

