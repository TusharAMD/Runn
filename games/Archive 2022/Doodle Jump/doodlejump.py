import pygame
import random
from settings import *
from pygame.locals import*
pygame.init()
font = pygame.font.SysFont(None,25)

def messageToScreen(msg,color,x,y):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[x,y])
    pygame.display.update()


clock=pygame.time.Clock()

gameDisplay=pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
pygame.display.set_caption("Doodle Jump!")
img_pikachu=pygame.image.load('pikachu.png').convert_alpha()
background=pygame.image.load('background.jpg').convert()


def gameLoop():

    gameExit = False
    lead_x = display_width / 2
    lead_y = display_height - 100
    lead_x_change = 0
    lead_y_change = 0
    vx=0
    vy=0
    g=1


    randObjectX=random.randrange(0,display_width)
    randObjectY=random.randrange(0,display_height)

    gameOver = False

    while not gameExit:

        while gameOver==True:
            gameDisplay.fill(white)
            messageToScreen("Game Over! Press A to Play Again. Press Q to quit!",red,display_width/2-220,display_height/2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a:
                        gameLoop()

                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True

            if event.type==pygame.K_SPACE:
                playerJumping=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change -= 10

                if event.key == pygame.K_RIGHT:
                    lead_x_change += 10

                if event.key == pygame.K_UP:
                    lead_y_change -= 10

                if event.key == pygame.K_DOWN:
                    lead_y_change += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x_change = 0

                if event.key == pygame.K_RIGHT:
                    lead_x_change = 0

                if event.key == pygame.K_UP:
                    lead_y_change = 0

                if event.key == pygame.K_DOWN:
                    lead_y_change = 0

        lead_x=lead_x+lead_x_change
        lead_y=lead_y+lead_y_change

        if lead_x==display_width:
            lead_x=0
        if lead_x==-50:
            lead_x=display_width
        if lead_y == display_height:
            gameOver=True
        if lead_y == -50:
            lead_y = display_height

        


        gameDisplay.fill(black)
        gameDisplay.blit(background, (0, 0))
        pygame.draw.rect(gameDisplay, red, [randObjectX, randObjectY, 100, 10])
        gameDisplay.blit(img_pikachu, (lead_x, lead_y))

        pygame.display.update()
       #pygame.draw.rect(gameDisplay,white,[lead_x,lead_y,block_width,block_height])
        messageToScreen("Welcome to DOODLE JUMP",red,display_width/2-100,display_height - 50)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameLoop()