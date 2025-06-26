from grid_system import GridSystem
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = GridSystem()
        self.blocks = [IBlock(),TBlock(),JBlock(),ZBlock(),LBlock(),OBlock(),SBlock()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()

    def random_block(self):
        if len(self.blocks)==0:
            self.blocks = [IBlock(),TBlock(),JBlock(),ZBlock(),LBlock(),OBlock(),SBlock()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)