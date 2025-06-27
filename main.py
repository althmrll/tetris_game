import pygame,sys
from game_mechanics import Game
from color_scheme import Colors

pygame.init()

title=pygame.font.Font(None,40)
score=title.render("Score:",True, Colors.text_color)
next_block=title.render("Next:", True,Colors.text_color)
game_over_message=title.render("Game Over", True, Colors.text_color)
score_rect=pygame.Rect(320,55,170,60)
next_block_rect=pygame.Rect(320,215,170,180)

screen = pygame.display.set_mode((500,620)) #main_window
pygame.display.set_caption("Tetris Game") #title of the window

clock=pygame.time.Clock() #Determines frame rate of game

game=Game()

game_update=pygame.USEREVENT
pygame.time.set_timer(game_update, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over==False:
                game.move_down()
            if event.key == pygame.K_SPACE and game.game_over==False:
                game.rotate()
        if event.type==game_update and game.game_over==False:
            game.move_down()

    screen.fill(Colors.line_color)
    screen.blit(score,(365,20,50,50))
    screen.blit(next_block,(370,180,50,50))
    if game.game_over==True:
        screen.blit(game_over_message,(330,450,50,50))
    pygame.draw.rect(screen,Colors.empty,score_rect,0,10)
    pygame.draw.rect(screen,Colors.empty,next_block_rect,0,10)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
