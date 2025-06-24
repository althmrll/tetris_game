import pygame

class GridSystem:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.grid=[[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors= self.block_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()
    
    def block_colors(self):
        red = (153,15,2)
        orange=(216,124,33)
        yellow = (255,246,0)
        green = (0,106,78)
        blue = (22,30,153)
        indigo=(0,157,175)
        violet = (53,28,117)

        return [red,orange,yellow,green,blue,indigo,violet]
    
    def draw(self,screen):
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size+1, row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)