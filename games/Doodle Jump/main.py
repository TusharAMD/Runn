import pygame
import random
from lowPlatform import *
from settings import *
from platforms import *
from enemies import *
from Clouds import *
vec=pygame.math.Vector2
from os import path


class Game:
    def __init__(self): #initialize game window and other things for the game.
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        self.gameDisplay.fill(white)
        pygame.display.set_caption("Doodle Jump!")
        self.clock = pygame.time.Clock()
        self.img_pikachu=pygame.sprite.Sprite()
        self.img_pikachu.image=pygame.image.load('pikachu.png').convert_alpha()
        self.img_pikachu.rect=self.img_pikachu.image.get_rect()
        #self.img_pikachu = pygame.image.load('pikachu.png').convert_alpha()
        self.background = pygame.image.load('blue_back.jpg').convert()
        self.font = pygame.font.SysFont(None, 25)
        self.gameExit = False
        self.pos=vec(display_width-100,display_height)
        self.img_pikachu.rect.topleft=[self.pos.x,self.pos.y]
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.playerSprite=pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.playerSprite.add(self.img_pikachu)
        p1 = lowPlatform(0, display_height - 40, display_width, 40)
        #p2 = Platform(display_width/2 - 50,display_height-150)
        #p3 = Platform(display_width/2 - 100,display_height-300)
        #p4 = Platform(display_width / 2, display_height - 450)
        #p5 = Platform(0, display_height - 600)
        platform_obj=Platform(self)
        self.platform_images=platform_obj.getImages()
        p2=Platform(self)
        p2.getPlatform(display_width/2 - 50,display_height-150,self.platform_images)
        p3 = Platform(self)
        p3.getPlatform(display_width/2 - 100,display_height-300, self.platform_images)
        p4 = Platform(self)
        p4.getPlatform(display_width / 2, display_height - 450, self.platform_images)
        p5 = Platform(self)
        p5.getPlatform(0, display_height - 600, self.platform_images)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.platforms.add(p3)
        self.platforms.add(p4)
        self.platforms.add(p5)
        self.score=0
        self.font_name=pygame.font.match_font(Font_Name)
        self.load_data()
        #pygame.mixer.music.load(path.join(self.sound_dir,'background_music.ogg'))
        self.enemies_timer=0

        for i in range(8):
            c=Cloud(self)
            c.rect.y+= 600

    def load_data(self):
        # loading the high score from the file
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, hs_file), 'r+') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # load cloud images
        cloud_dir = path.join(self.dir, 'clouds_img')
        self.cloud_images=[]
        for i in range(1,4):
            self.cloud_images.append(pygame.image.load(path.join(cloud_dir,'cloud{}.png'.format(i))).convert())

        # load sounds
        self.sound_dir=path.join(self.dir,'sound')
        self.jump_sound=pygame.mixer.Sound(path.join(self.sound_dir,'jump.ogg'))
        self.jump_sound.set_volume(0.1)
        self.pow_sound = pygame.mixer.Sound(path.join(self.sound_dir, 'pow.wav'))

    def updateScreen(self):

        now_time=pygame.time.get_ticks()
        if now_time-self.enemies_timer>5000 + random.choice([-1000,-500,0,500,1000]):
            self.enemies_timer=now_time
            Enemies(self)

        enemies_hits=pygame.sprite.spritecollide(self.img_pikachu,self.enemies,False, pygame.sprite.collide_mask)
        if enemies_hits:
            self.gameOver=True

        #Updating the sprite's position
        self.img_pikachu.rect.midbottom = [self.pos.x, self.pos.y]
        #Checking for collision between the player and the sprites.
        powerup_hits = pygame.sprite.spritecollide(self.img_pikachu, self.powerups, False)
        for x in powerup_hits:
            self.pow_sound.play()
            self.vel.y = power_up_boost

        if self.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.img_pikachu, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit

                if self.pos.x < lowest.rect.right + 30 and self.pos.x > lowest.rect.left - 30:
                    if self.pos.y < lowest.rect.centery:
                        self.pos.y = lowest.rect.top
                        self.vel.y = 0

        #Scrolling the screen upwards as the player moves upward. Killing the platforms which are not futher required.
        if self.img_pikachu.rect.top <= display_height/4:

            if random.randrange(100) < 99:
                Cloud(self)

            self.pos.y+=abs(self.vel.y)

            for cloud in self.clouds:
                cloud.rect.y+=max(abs(self.vel.y / 2), 2)

            for platform in self.platforms:
                platform.rect.y+=abs(self.vel.y)
                if platform.rect.top>=display_height:
                    platform.kill()
                    self.score+=10

            for enemy in self.enemies:
                 enemy.rect.y += abs(self.vel.y)





         #GAME OVER CHECK.
        if self.img_pikachu.rect.bottom>display_height:
            self.gameOver=True;
            for sprite in self.platforms:
                sprite.rect.y-=max(self.vel.y,10)

        #Creating new platforms.
        while len(self.platforms)<6:#There should be atleast 6 platforms on the screen.
            width=random.randrange(50,100)
            p = Platform(self)
            p.getPlatform(random.randrange(0,display_width-width), random.randrange(-50,-30), self.platform_images)
            self.platforms.add(p)

        for x in self.powerups: #updating powerup sprites positions according to the change in platform position.
            x.update()


        self.gameDisplay.fill(black)
        self.enemies.update()
        self.powerups.update()
        self.platforms.update()
        self.clouds.update()
        self.playerSprite.update( )
        self.gameDisplay.blit(self.background,(0,0))
        self.clouds.draw(self.gameDisplay)
        self.platforms.draw(self.gameDisplay)
        self.powerups.draw(self.gameDisplay)
        self.enemies.draw(self.gameDisplay)

        self.playerSprite.draw(self.gameDisplay)
        # pygame.draw.rect(self.gameDisplay, red, [randObjectX, randObjectY, 100, 10])
        #self.gameDisplay.blit(self.img_pikachu, (self.pos.x, self.pos.y))
        #Displaying the score.
        self.messageToScreen("SCORE : "+(str)(self.score), 25, white, display_width / 2 , 15)
        pygame.display.update()
        # pygame.draw.rect(gameDisplay,white,[lead_x,lead_y,block_width,block_height])
        #self.messageToScreen("Welcome to DOODLE JUMP", red, display_width / 2 - 100, display_height - 20)


    def run(self):
       # pygame.mixer.music.play(loops=-1)
        #pygame.mixer.music.set_volume(0.5)
        self.score=0
        self.gameOver = False
        while not self.gameExit:
            self.checkEvent()
            self.acc.x+=self.vel.x*player_Fric
            self.vel+=self.acc
            self.pos+=self.vel+0.5*self.acc
            self.checkHorizontalCrossing()
            self.updateScreen()
            self.clock.tick(fps)
            if self.gameOver==True:
                self.gameOverScreen()
        pygame.mixer.music.fadeout(500)

        pygame.quit()
        quit()

    def checkHorizontalCrossing(self):
        if self.pos.x > display_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = display_width
        if self.pos.y == display_height:
            self.gameOver = True
        if self.pos.y == -50:
            self.pos.y = display_height

    def checkEvent(self):
        self.acc=vec(0,gravity)
        self.jump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.acc.x = -player_Acc

                if event.key == pygame.K_RIGHT:
                    self.acc.x = player_Acc

                if event.key == pygame.K_SPACE:
                    self.jump()


    def messageToScreen(self,msg,size, color, x, y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(msg,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.gameDisplay.blit(text_surface,text_rect)

    def jump(self):

            #We check if the player sprite is standing on a platform on or not.
            if self.vel.y>0:
                self.img_pikachu.rect.y+=1
                hits=pygame.sprite.spritecollide(self.img_pikachu,self.platforms,False)
                self.img_pikachu.rect.y -= 1
                if hits:
                    self.jump_sound.play()
                    self.vel.y = -10

    def startScreen(self):
        self.gameDisplay.fill(orange)
        self.messageToScreen("DOODLE JUMP MP PROJECT - II",40,white,display_width/2,display_height/2)
        self.messageToScreen("Press any key to continue...", 25, white, display_width / 2 + 50, display_height / 2 + 50)
        self.messageToScreen("High Score: " + str(self.highscore), 25, white, display_width / 2, 35)
        pygame.display.update()
        self.waitForKeyPress()
        g.run()


    def gameOverScreen(self):
        self.gameDisplay.fill(orange)
        self.messageToScreen("OOPS!...GAME-OVER", 40, white, display_width / 2, 180)
        self.messageToScreen("Score : "+(str)(self.score), 40, white, display_width / 2, display_height / 2-100)
        self.messageToScreen("Press any key to play again...", 30, white, display_width / 2 + 50, display_height / 2 + 50)

        if self.score > self.highscore:
            self.highscore = self.score
            self.messageToScreen("CONGRATULATIONS!!!  NEW HIGH SCORE!", 30, white, display_width / 2, display_height / 2 - 30)
            with open(path.join(self.dir, hs_file), 'w') as f:                      # writing the new highscore in the file
                f.write(str(self.score))
        else:
                self.messageToScreen("High Score: " + str(self.highscore), 30, white, display_width / 2, display_height / 2 - 30)

        pygame.display.update()
        self.waitForKeyPress()
        g.__init__()
        g.run()

    def waitForKeyPress(self):
        waiting=True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.gameExit=True
                if event.type==pygame.KEYUP:
                    waiting=False
                    self.gameOver=False
                    self.gameExit=False

g=Game()
g.startScreen()
