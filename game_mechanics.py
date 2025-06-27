from grid_system import GridSystem
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = GridSystem()
        self.blocks = [IBlock(),TBlock(),JBlock(),ZBlock(),LBlock(),OBlock(),SBlock()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.game_over=False
        self.score=0
    
    def update_score(self,lines_cleared):
       if lines_cleared>=1:
           points=lines_cleared*100
           self.score+=points

    def random_block(self):
        if len(self.blocks)==0:
            self.blocks = [IBlock(),TBlock(),JBlock(),ZBlock(),LBlock(),OBlock(),SBlock()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.inside_checker()==False or self.check_if_block_fits()==False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.inside_checker()==False or self.check_if_block_fits()==False:
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)
        if self.inside_checker()==False or self.check_if_block_fits()==False:
            self.current_block.move(-1,0)
            self.lock_in_place()

    def lock_in_place(self):
        tiles=self.current_block.get_position()
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        self.current_block=self.next_block
        self.next_block=self.random_block()
        cleared_rows=self.grid.clear_full_row()
        self.update_score(cleared_rows)
        if self.check_if_block_fits()==False:
            self.game_over=True
    
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(),TBlock(),JBlock(),ZBlock(),LBlock(),OBlock(),SBlock()]
        self.current_block=self.random_block()
        self.next_block=self.random_block()
        self.score=0

    def rotate(self):
        self.current_block.rotate()
        if self.inside_checker()==False or self.check_if_block_fits()==False:
            self.current_block.undo_rotation(0)

    def inside_checker(self):
        tiles=self.current_block.get_position()
        for tile in tiles:
            if self.grid.block_position_limit(tile.row,tile.column)==False:
                return False
        return True
    
    def check_if_block_fits(self):
        tiles=self.current_block.get_position()
        for tile in tiles:
            if self.grid.check_if_empty(tile.row,tile.column)==False:
                return False
        return True
    
    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11,11)
        if self.next_block.id==1:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id==6:
            self.next_block.draw(screen,255,280)
        else:
            self.next_block.draw(screen,270,270)