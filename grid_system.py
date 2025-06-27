import pygame
from color_scheme import Colors

class GridSystem:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.grid=[[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors= Colors.block_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()
    
    def block_position_limit(self, row, column):
        if row>=0 and row<self.num_rows and column>=0 and column<self.num_cols:
            return True
        return False

    def undo_rotate(self):
        self.rotation_state+=1
        if self.rotation_state==0:
            self.rotation_state = len(self.cells)-1

    def check_if_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def check_if_row_is_full(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column]==0:
                return False
        return True
        
    def clear_cell_value(self,row):
        for column in range(self.num_cols):
            self.grid[row][column]=0
    
    def move_row_down(self,row,num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column]=self.grid[row][column]
            self.grid[row][column]=0
        
    def clear_full_row(self):
        completed=0
        for row in range(self.num_rows-1,0,-1):
            if self.check_if_row_is_full(row):
                self.clear_cell_value(row)
                completed+=1
            elif completed>0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column]=0

    def draw(self,screen):       
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size+11, row*self.cell_size+11,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)