from itertools import filterfalse
import pygame
import os
import random
import sys

pygame.init()

SCREEN_HEIGHT=700
SCREEN_WIDTH=700
SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
RUNNING=[pygame.image.load(os.path.join("assets/mainchar","sprite_0.png")),
         pygame.image.load(os.path.join("assets/mainchar","sprite_1.png")),
         pygame.image.load(os.path.join("assets/mainchar","sprite_2.png"))]
FLOWER=[pygame.image.load(os.path.join("assets","flower.png"))]
ROCK=[pygame.image.load(os.path.join("assets","rock.png"))]
BCKGRD=[pygame.image.load(os.path.join("assets/road","sprite_0.png")),
         pygame.image.load(os.path.join("assets/road","sprite_1.png")),
         pygame.image.load(os.path.join("assets/road","sprite_2.png"))]

for i in range(len(RUNNING)):
    RUNNING[i]=pygame.transform.scale(RUNNING[i],(140,140))
for i in range(len(BCKGRD)):
    BCKGRD[i]=pygame.transform.scale(BCKGRD[i],(700,700))
ROCK[0]=pygame.transform.scale(ROCK[0],(50,50))

FLOWER[0]=pygame.transform.scale(FLOWER[0],(70,70))

class State:
    
    def __init__(self):
        self.main_menu = True
        self.flower_game_start = False


        self.stone_collision = False
        self.flower_collision = False

class Menu:

    def __init__(self):
        self.bg_color = (255,255,255)
        self.text_color = (50,50,50)
        self.font_50 =  pygame.font.Font("assets/font.otf", 50)
        self.font_80 =  pygame.font.Font("assets/font.otf", 80)
        
        self.start_image = self.font_50.render("Press Space To Start" , True , self.text_color , self.bg_color)
        self.start_image_rect = self.start_image.get_rect()
        self.mp_x = SCREEN_WIDTH/2 - self.start_image_rect[2]/2
        self.mp_y = 2*SCREEN_HEIGHT/3 - self.start_image_rect[3]/2 

        self.game_name_image = self.font_80.render("Runn" , True , self.text_color , self.bg_color)
        self.game_name_image_rect = self.game_name_image.get_rect()
        self.game_name_x = SCREEN_WIDTH/2 - self.game_name_image_rect[2]/2
        self.game_name_y = SCREEN_HEIGHT/3 - self.game_name_image_rect[3]/2 

    def  draw_mainmenu(self , SCREEN):
        SCREEN.blit(self.game_name_image , [self.game_name_x , self.game_name_y])
        SCREEN.blit(self.start_image , [self.mp_x , self.mp_y])

class mainCharacter:
    X_POS=280
    Y_POS=450

    

    def __init__(self):
        self.run_img=RUNNING
        
        self.run=True

        self.step_index=0
        self.image=self.run_img[0]
        self.rect=self.image.get_rect()

        self.rect.x=self.X_POS
        self.rect.y=self.Y_POS

    def update(self,userInput):
        if self.run:
            self.run_func()

        if self.step_index ==3:
            self.step_index=0


        if userInput[pygame.K_UP]:
            self.run=True
            self.X_POS=280
        elif userInput[pygame.K_LEFT]:
            self.run=True
            self.X_POS=130
        elif userInput[pygame.K_RIGHT]:
            self.run=True
            self.X_POS=430

        

    def run_func(self):
        self.image=self.run_img[self.step_index]
        self.rect=self.image.get_rect()
        self.rect.x=self.X_POS
        self.rect.y=self.Y_POS

        self.step_index+=1
        self.run=True

    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

class background:
    X_POS=0
    Y_POS=0

    def __init__(self):
        self.run_img=BCKGRD
        self.run=True
        self.step_index=0
        self.image=self.run_img[0]
        self.rect=self.image.get_rect()
        self.rect.x=self.X_POS
        self.rect.y=self.Y_POS

    def update(self): 
        if self.run:
            self.run_func()
        if self.step_index ==3:
            self.step_index=0
    def run_func(self):
        self.image=self.run_img[self.step_index]
        self.rect=self.image.get_rect()
        self.rect.x=self.X_POS
        self.rect.y=self.Y_POS
        pygame.time.Clock().tick(10)
        self.step_index+=1
        self.run=True

    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

def score():
    global points, game_speed, collisions, scoregain
    global initial
    font=pygame.font.Font('freesansbold.ttf',20)
    points=points+1

    text=font.render("Distance Covered:"+str(points),True,(100,0,50))
    textRect = text.get_rect()
    textRect.center=(500,20)
    SCREEN.blit(text,textRect)
    text=font.render("Collisions:"+str(collisions),True,(100,0,50))
    textRect = text.get_rect()
    textRect.center=(500,40)
    SCREEN.blit(text,textRect)
    text=font.render("Score:"+str(scoregain),True,(100,0,50))
    textRect = text.get_rect()
    textRect.center=(500,60)
    SCREEN.blit(text,textRect)

    text=font.render("Total:"+str((scoregain*5)+int(points/3)-(collisions*10)),True,(100,0,0))
    textRect = text.get_rect()
    textRect.center=(300,20)
    SCREEN.blit(text,textRect)
    
    
class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image[0].get_rect()
        self.rect.y = SCREEN_HEIGHT

    def update(self):
        game_speed2=random.randint(10,25)
        self.rect.y += game_speed
        if self.rect.y > 500:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[0], self.rect)

class NOTObstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image[0].get_rect()
        self.rect.y = SCREEN_HEIGHT

    def update(self):
        game_speed2=random.randint(10,50)
        self.rect.y += game_speed2
        if self.rect.y > 500:
            gainers.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[0], self.rect)


class Stone(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 0
        self.rect.x = random.choice([210,340,490])

class Flower(NOTObstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 0
        self.rect.x = random.choice([210,340,490])

def main():
    global game_speed, xposbg,yposbg,points,obstacles,collisions,scoregain, gainers
    points=0
    collisions=0
    scoregain=0
    
    obstacles=[]

    gainers=[]
    game_speed=14
    run=True
    clock=pygame.time.Clock()
    player=mainCharacter()
    bg=background()
    state = State()
    menu = Menu()
    pygame.display.set_caption("Runn")

    while run:

        

        pygame.event.get()
        SCREEN.fill((255,255,255))
        userInput=pygame.key.get_pressed()


        
        
        if state.flower_game_start==True:

            bg.draw(SCREEN)
            bg.update()
            score()
            if len(obstacles) == 0:
                obstacles.append(Stone(ROCK))

            if len(gainers) == 0:
                gainers.append(Flower(FLOWER))

            for obstacle in obstacles:
                obstacle.draw(SCREEN)
                obstacle.update()
                if player.rect.colliderect(obstacle.rect):
                    #pygame.draw.rect(SCREEN,(255,0,0),player.rect,2)
                    if state.stone_collision == False:
                        collisions+=1
                    state.stone_collision = True
                    continue
                else:
                    state.stone_collision = False
                    #print(collisions)
            for fl in gainers:
                fl.draw(SCREEN)
                fl.update()
                if player.rect.colliderect(fl.rect):
                    #pygame.draw.rect(SCREEN,(0,255,0),player.rect,2)
                    if state.flower_collision == False:
                        scoregain+=1
                    state.flower_collision = True
                    continue
                else:
                    state.flower_collision = False
        
            player.draw(SCREEN)
            player.update(userInput)      
        elif state.main_menu==True:
            menu.draw_mainmenu(SCREEN)
            
        pygame.display.update()

        # enable quit functionality in pygame
        for event in pygame.event.get():

            run = False if event.type == pygame.QUIT else True

            if event.type == pygame.KEYDOWN:
                if state.main_menu==True:
                    if event.key == pygame.K_SPACE:
                        state.main_menu = False
                        state.flower_game_start = True
                    
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                
                if state.flower_game_start == True:
                    if event.key == pygame.K_ESCAPE:
                        state.main_menu = True
                        state.flower_game_start = False
                        points=0
                        collisions=0
                        scoregain=0


if __name__ == '__main__':
    main()
