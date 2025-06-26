import pygame,sys
from game_mechanics import Game

#variables
line_color=(45,59,67)

pygame.init()

screen = pygame.display.set_mode((300,600)) #main_window
pygame.display.set_caption("Tetris Game") #title of the window

clock=pygame.time.Clock() #Determines frame rate of game
screen.fill(line_color)

game=Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_SPACE:
                game.rotate()

    pygame.display.update()
    clock.tick(60)
    game.draw(screen)
