import pygame,sys
from grid_system import GridSystem

#variabless
line_color=(45,59,67)

pygame.init()

screen = pygame.display.set_mode((300,600)) #main_window
pygame.display.set_caption("Tetris Game") #title of the window

clock=pygame.time.Clock() #Determines frame rate of game
game_grid=GridSystem()
game_grid.grid[0][0]=1
game_grid.grid[3][5]=4
game_grid.grid[17][8]=7
game_grid.print_grid()

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
