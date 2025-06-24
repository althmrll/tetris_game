from color_scheme import Colors
from block_position import BlockPosition
import pygame

class GeneralBlock:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cell_size=30
        self.row_offset=0
        self.column_offset=0
        self.rotation_state=0
        self.colors=Colors.block_colors()
    
    def move(self,rows,columns):
        self.row_offset+=rows
        self.column_offset+=columns
    
    def get_position(self,screen):
        tiles=self.cells[self.rotation_state]
        moved_tiles=[]
        for position in tiles:
            position=BlockPosition(position.row+self.row_offset, position.column+self.column_offset)
            moved_tiles.append(position)
            return moved_tiles
        
    def draw(self, screen):
        tiles=self.get_position
        for tile in tiles:
            tile_rect=pygame.Rect(tile.column*self.cell_size+1, tile.row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
            pygame.draw.rect(screen,self.colors[self.id], tile_rect)