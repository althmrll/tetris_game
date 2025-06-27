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
        
    def draw(self,screen):       
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size+1, row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)