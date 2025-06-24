import pygame,sys
from grid_system import GridSystem
from blocks import *

#variables
line_color=(45,59,67)

pygame.init()

screen = pygame.display.set_mode((300,600)) #main_window
pygame.display.set_caption("Tetris Game") #title of the window

clock=pygame.time.Clock() #Determines frame rate of game
game_grid=GridSystem()

block=IBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
    clock.tick(60)

#design
    screen.fill(line_color)
    game_grid.draw(screen)
    block.draw(screen)