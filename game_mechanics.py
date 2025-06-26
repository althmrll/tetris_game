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
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.inside_checker()==False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.inside_checker()==False:
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)
        if self.inside_checker()==False:
            self.current_block.move(-1,0)
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside()==False:
            self.current_block.undo_rotation(0)

    def inside_checker(self):
        tiles=self.current_block.get_position()
        for tile in tiles:
            if self.grid.block_position_limit(tile.row,tile.column)==False:
                return False
        return True

    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)