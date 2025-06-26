from grid_system import GridSystem
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = GridSystem()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()

    def random_block(self):
        ...