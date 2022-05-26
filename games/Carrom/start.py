import pygame, sys,math
from pygame.locals import *
from math import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
background=(255,255,255)
screen.fill(background)
pygame.display.set_caption("Carrom")
width=535
height=535
friction=0.2
border=65
mod = lambda v: sqrt(v[0] * v[0] + v[1] * v[1])
black=(0,0,0)
player1_color=(40,40,40)
player2_color=(180,180,180)
white=(255,255,255)
yellow=(255,255,0)
pink=(255,20,147)
def repaint():    
    pygame.draw.rect(screen,(0,0,0),Rect((40,40),(520,520)))
    pygame.draw.rect(screen,(230,210,140),Rect((65,65),(470,470)))
    pygame.draw.rect(screen,(0,0,0),Rect((180,140),(240,20)))
    pygame.draw.rect(screen,(230,210,140),Rect((185,145),(230,10)))
    pygame.draw.circle(screen,(139,0,0),(180,150),10)
    pygame.draw.circle(screen,(139,0,0),(420,150),10)
    pygame.draw.rect(screen,(0,0,0),Rect((180,440),(240,20)))
    pygame.draw.rect(screen,(230,210,140),Rect((185,445),(230,10)))
    pygame.draw.circle(screen,(160,0,0),(180,450),10)
    pygame.draw.circle(screen,(160,0,0),(420,450),10)
    pygame.draw.rect(screen,(0,0,0),Rect((140,180),(20,240)))
    pygame.draw.rect(screen,(230,210,140),Rect((145,185),(10,230)))
    pygame.draw.circle(screen,(139,0,0),(150,180),10)
    pygame.draw.circle(screen,(139,0,0),(150,420),10)
    pygame.draw.rect(screen,(0,0,0),Rect((440,180),(20,240)))
    pygame.draw.rect(screen,(230,210,140),Rect((445,185),(10,230)))
    pygame.draw.circle(screen,(139,0,0),(450,180),10)
    pygame.draw.circle(screen,(139,0,0),(450,420),10)
    pygame.draw.circle(screen,(139,0,0),(300,300),60,2)
    pygame.draw.circle(screen,(139,0,0),(300,300),70,2)
    pygame.draw.circle(screen,(139,10,0),(300,300),20,4)
    pygame.draw.circle(screen,(139,10,0),(300,300),11,0)
    pygame.draw.circle(screen,white,(80,80),20)
    pygame.draw.circle(screen,white,(520,80),20)
    pygame.draw.circle(screen,white,(80,520),20)
    pygame.draw.circle(screen,white,(520,520),20)
def move(coin1,coin2):    
    center1 = [coin1.rect.x+coin1.radius, coin1.rect.y+coin1.radius]
    center2 = [coin2.rect.x+coin2.radius, coin2.rect.y+coin2.radius]
    distx = abs(center1[0]-center2[0])
    disty = abs(center1[1]-center2[1])
    #the distance between the centers of coins
    dist = [abs(center1[0]-center2[0]), abs(center1[1]-center2[1])]
    if mod(dist)==0:
        cos_theta = 1
        sin_theta = 0
    else:
        cos_theta = abs(distx)/mod(dist)
        sin_theta = abs(disty)/mod(dist)
    if mod(dist)<coin1.radius + coin2.radius:
        diff = coin1.radius + coin2.radius - mod(dist)        
        if coin2.rect.x>=coin1.rect.x:
            coin2.rect.x += ceil(diff*cos_theta/2)
            coin1.rect.x -= ceil(diff*cos_theta/2)
        else:
            coin1.rect.x += ceil(diff*cos_theta/2)
            coin2.rect.x -= ceil(diff*cos_theta/2)
        if coin2.rect.y>=coin1.rect.y:
            coin2.rect.y += ceil(diff*cos_theta/2)
            coin1.rect.y -= ceil(diff*cos_theta/2)
        else:
            coin1.rect.y += ceil(diff*cos_theta/2)
            coin2.rect.y += ceil(diff*cos_theta/2)
def collision(coin1,coin2):    
    v=(coin1.rect.x-coin2.rect.x,coin1.rect.y-coin2.rect.y)  
    m=math.sqrt(math.pow(v[0],2)+math.pow(v[1],2))    
    if m>0:
        n=(v[0]/m,v[1]/m)
    else:
        n=(0,0)    
    t=((-n[1]),n[0])
    move(coin1,coin2)   
    v_r=(coin1.velx,coin1.vely)
    v_s=(coin2.velx,coin2.vely)
    v_rnormal=(v_r[0]*n[0])+(v_r[1]*n[1])
    v_rtangent=(v_r[0]*t[0])+(v_r[1]*t[1])
    v_snormal=(v_s[0]*n[0])+(v_s[1]*n[1])
    v_stangent=(v_s[0]*t[0])+(v_s[1]*t[1])
    v_rnn=v_snormal*0.75
    v_snn=v_rnormal*0.75
    v_rnormal=((v_rnn*n[0]),(v_rnn*n[1]))
    v_snormal=((v_snn*n[0]),(v_snn*n[1]))
    v_rtangent=((v_rtangent*t[0]),(v_rtangent*t[1]))
    v_stangent=((v_stangent*t[0]),(v_stangent*t[1]))
    v_r=((v_rnormal[0]+v_rtangent[0]),(v_rnormal[1]+v_rtangent[1]))
    v_s=((v_snormal[0]+v_stangent[0]),(v_snormal[1]+v_stangent[1]))
    coin1.velx=v_r[0]
    coin1.vely=v_r[1]
    coin2.velx=v_s[0]
    coin2.vely=v_s[1]
def inhole(sprite):
    (centerx,centery)=sprite.rect.center
    a=78
    b=522
    dist= math.sqrt((centerx-a)**2 + (centery-a)**2)
    if dist<=(2*sprite.radius+20)/3:
        return True
    dist= math.sqrt((centerx-a)**2 + (centery-b)**2)
    if dist<=(2*sprite.radius+20)/3:
         return True
    dist= math.sqrt((centerx-b)**2 + (centery-a)**2)
    if dist<=(2*sprite.radius+20)/3:
        return True
    dist= math.sqrt((centerx-b)**2 + (centery-b)**2)
    if dist<=(2*sprite.radius+20)/3:
         return True
    return False         
class Coins(pygame.sprite.Sprite):
    def __init__(self,radius,colour):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([(2*radius),(2*radius)])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.ellipse(self.image,colour,[0,0,(2*radius),(2*radius)])
        self.rect=self.image.get_rect()
        self.radius=radius
        self.angle=0
        self.velx=0
        self.vely=0
        self.collided=False
        self.colour=colour        
    def collide(self,coin_array):
        for coin in coin_array:
            if coin!= self:
                self.other_list.add(coin)
        for coin in self.other_list:
            collision(self,coin)                            
    def update(self):
        self.rect.x +=self.velx
        self.rect.y +=self.vely

        if (self.rect.x) > width-(2*self.radius):
               self.rect.x = 2*(width - (2*self.radius)) - self.rect.x
               self.velx = -1*abs(self.velx)

        elif (self.rect.x) < (65):
               self.rect.x = 2*(65)- self.rect.x
               self.velx = abs(self.velx)

        if (self.rect.y) > height-(2*self.radius):
               self.rect.y = 2*(height - (2*self.radius)) - self.rect.y
               self.vely = -1*abs(self.vely)

        elif (self.rect.y) < (65):
               self.rect.y = 2*(65) - self.rect.y
               self.vely = abs(self.vely)
        if mod([self.velx, self.vely])==0:
            self.velx = 0
            self.vely = 0
        else:
            self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely]) 
            self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely]) 
            if abs(self.velx)<friction:
                self.velx = 0
            if abs(self.vely)<friction:
                self.vely = 0        
coin_list=pygame.sprite.Group()
coin_array=pygame.sprite.Group()
striker=Coins(15,(255,240,120))
striker.rect.x=282
striker.rect.y=435
coin_array.add(striker)
coin11=Coins(11,player2_color)
coin11.rect.x=288
coin11.rect.y=288-27
coin_array.add(coin11)
coin_list.add(coin11)
coin22=Coins(11,player2_color)
coin22.rect.x=288
coin22.rect.y=288+27
coin_array.add(coin22)
coin_list.add(coin22)
coin3=Coins(11,player2_color)
coin3.rect.x=288-27
coin3.rect.y=288
coin_array.add(coin3)
coin_list.add(coin3)
coin4=Coins(11,player2_color)
coin4.rect.x=288+27
coin4.rect.y=288
coin_array.add(coin4)
coin_list.add(coin4)
coin6=Coins(11,player1_color)
coin6.rect.x=288+21
coin6.rect.y=288+21
coin_array.add(coin6)
coin_list.add(coin6)
coin7=Coins(11,player1_color)
coin7.rect.x=288+21
coin7.rect.y=288-21
coin_array.add(coin7)
coin_list.add(coin7)
coin8=Coins(11,player1_color)
coin8.rect.x=288-21
coin8.rect.y=288+21
coin_array.add(coin8)
coin_list.add(coin8)
coin9=Coins(11,player1_color)
coin9.rect.x=288-21
coin9.rect.y=288-21
coin_array.add(coin9)
coin_list.add(coin9)
coin10=Coins(11,player2_color)
coin10.rect.x=288-38
coin10.rect.y=288-38
coin_array.add(coin10)
coin_list.add(coin10)
coin11=Coins(11,player2_color)
coin11.rect.x=288-38
coin11.rect.y=288+38
coin_array.add(coin11)
coin_list.add(coin11)
coin12=Coins(11,player2_color)
coin12.rect.x=288+38
coin12.rect.y=288-38
coin_array.add(coin12)
coin_list.add(coin12)
coin13=Coins(11,player2_color)
coin13.rect.x=288+38
coin13.rect.y=288+38
coin_array.add(coin13)
coin_list.add(coin13)
coin14=Coins(11,player2_color)
coin14.rect.x=288-36
coin14.rect.y=288+38
coin_array.add(coin14)
coin_list.add(coin9)
coin15=Coins(11,player1_color)
coin15.rect.x=288
coin15.rect.y=288-49
coin_array.add(coin15)
coin_list.add(coin15)
coin16=Coins(11,player1_color)
coin16.rect.x=288-49
coin16.rect.y=288
coin_array.add(coin16)
coin_list.add(coin16)
coin17=Coins(11,player1_color)
coin17.rect.x=288+49
coin17.rect.y=288
coin_array.add(coin17)
coin_list.add(coin17)
coin18=Coins(11,player1_color)
coin18.rect.x=288
coin18.rect.y=288+49
coin_array.add(coin18)
coin_list.add(coin18)
queen=Coins(11,(255,30,177))
queen.rect.x=289
queen.rect.y=289
coin_array.add(queen)
coin_list.add(queen)
repaint()
coin_array.draw(screen)
clock=pygame.time.Clock()
speed=200
attempt=0
queen_gone_temp=0
queen_gone_final=0
x=300
y=450
movex=0
movey=0
flag=0
degree=0.04
i=0
player=0
player1_points=0
player2_points=0
foul=0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        
        if flag==0:
            if player==0:
                x,y=pygame.mouse.get_pos()
                y=450;
                
                if(x<180):
                     x=180
                if(x>420):
                     x=420
            else:
                x,y=pygame.mouse.get_pos()
                y=150;
                
                if(x<180):
                     x=180
                if(x>420):
                     x=420               
            striker.rect.x=x-striker.radius
            striker.rect.y=y-striker.radius
            striker_center=(striker.rect.x+striker.radius,striker.rect.y+striker.radius)
            repaint()
            coin_array.draw(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:             
            if flag==0:
                flag=1               
            elif flag==1:
                flag=2         
        if flag==1:
            x_point,y_point=pygame.mouse.get_pos()
            if player==0:#down player
                if(y_point<470):
                     y_point=480
                if(y_point>535):
                    y_point=535
                if(x_point<65):
                    x_point=65
                if(x_point>535):
                    x_point=535
            if player==1:
                if(y_point>120):
                     y_point=120
                if(y_point<65):
                    y_point=65
                if(x_point<65):
                    x_point=65
                if(x_point>535):
                    x_point=535            
            repaint()
            coin_array.draw(screen)
            line=pygame.draw.line(screen,black,(striker_center[0],striker_center[1]),(x_point,y_point),3)                    
        if flag==2:
            flag=3
            i=25
            striker.velx=(striker_center[0]-x_point)/4
            striker.vely=(striker_center[1]-y_point)/4             
    if flag==3:         
        coin_array.update()        
        for coin1 in coin_array:
            for coin2 in coin_list:
                if coin1 is not coin2 and pygame.sprite.collide_circle(coin1, coin2) and not coin1.collided and not coin2.collided:
                    collision(coin1, coin2)
                    for coin1 in coin_list:
                        for coin2 in coin_list:
                            if coin1 is not coin2:
                                move(coin1, coin2)                        
                    coin1.collided, coin2.collided = True, True                   
        for coin in coin_array:
            coin.collided = False
            if inhole(coin):
                if coin is not striker:
                    coin_array.remove(coin)
                    coin_array.remove(coin)
                    if coin.colour==(255,30,177):
                        queen_gone_temp=1                                             
                    if coin.colour==player1_color:
                        if queen_gone_temp==1:
                            player1_points+=5
                            queen_gone_final=1
                            coin_array.remove(queen)                            
                        else:                            
                            player1_points+=1                            
                    elif coin.colour==player2_color:
                        if queen_gone_temp==1:
                            player2_points+=5
                            queen_gone_final=1
                            coin_queen.remove(queen)
                            attempt=1
                        else:
                            player2_points+=1
                    else:
                        if queen_gone_temp==1:
                            attempt=1
                        print ('Player1 Points= {}'.format(player1_points,"\n"))
                        print ('Player2 Points= {}'.format(player2_points,"\n"))
                if coin is not queen and not striker:
                    if queen_gone_temp==1 and attempt==1:
                        queen=Coins(11,(255,30,177))
                        queen.rect.x=289
                        queen.rect.y=289
                        coin_array.add(queen)
                        coin_list.add(queen)                                           
                if coin is striker:
                    print ("foul")
                    if player==0:
                        player1_points-=1
                    else:
                        player2_points-=1
                    coin_array.remove(striker)
                    foul=1                                                             
        repaint()
        coin_array.draw(screen)
    boardHalt = True    
    for coin in coin_array:
        if coin.velx!=0 or coin.vely!=0:
            boardHalt = False
            break    
    if boardHalt and flag==3:
            x=300
            y=450
            flag=0
            striker.velx=0
            striker.vely=0
            striker.angle=0
            coin_array.vely=0
            coin_array.velx=0         
            if(foul==1):
                striker=Coins(15,(255,240,120))
                coin_array.add(striker)
                foul=0
            if player==0:
                player=1
            else:
                player=0                               
    pygame.display.update()
    clock.tick(100)