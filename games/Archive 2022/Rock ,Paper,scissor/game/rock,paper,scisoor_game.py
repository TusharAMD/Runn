#import libraries
import random
import time
import cv2
import numpy as np
import mediapipe as mp

#player score and computer score
global pscore
pscore=0
global cscore
cscore=0
global g
g=False

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
tipId=[4,8,12,16,20]

#images for displaying text(rock,paper,scissor)
rock_img=cv2.imread('rock_image2.png')
rock_img=cv2.resize(rock_img,(160,40))

paper_img=cv2.imread('paper_image.png')
paper_img=cv2.resize(paper_img,(160,40))

scissor_img=cv2.imread('scissor_image.png')
scissor_img=cv2.resize(scissor_img,(160,40))

invalid_img=cv2.imread('invalid.png')
invalid_img=cv2.resize(invalid_img,(160,40))

imgsList=[rock_img,paper_img,scissor_img,invalid_img]

#function to recognise the player's action
def player(frame):
    y2=4
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(framergb)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList=[]                  
            for id,lm in enumerate(handLms.landmark):
                h,w,c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                    
            
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
        if lmList[tipId[2]][1]<lmList[tipId[1]][1]:
            if lmList[tipId[1]][2]< lmList[tipId[1]-1][2] and lmList[tipId[2]][2]< lmList[tipId[2]-1][2] and lmList[tipId[3]][2]> lmList[tipId[3]-1][2] and lmList[tipId[4]][2]> lmList[tipId[4]-1][2]:
                y2=3
                
            elif lmList[tipId[1]][2]< lmList[tipId[1]-1][2] and lmList[tipId[2]][2]< lmList[tipId[2]-1][2] and lmList[tipId[3]][2]< lmList[tipId[3]-1][2] and lmList[tipId[4]][2]< lmList[tipId[4]-1][2]:
                y2=2
                
            else: 
                y2=1   
        elif lmList[tipId[2]][1]<lmList[tipId[1]][1]:
            if lmList[tipId[1]][2]< lmList[tipId[1]-1][2] and lmList[tipId[2]][2]< lmList[tipId[2]-1][2] and lmList[tipId[3]][2]> lmList[tipId[3]-1][2] and lmList[tipId[4]][2]> lmList[tipId[4]-1][2]:
                y2=3
                
            elif lmList[tipId[1]][2]< lmList[tipId[1]-1][2] and lmList[tipId[2]][2]< lmList[tipId[2]-1][2] and lmList[tipId[3]][2]< lmList[tipId[3]-1][2] and lmList[tipId[4]][2]< lmList[tipId[4]-1][2]:
                y2=2
                
            else: 
                y2=1           
            
    return y2        
    
#on selecting play the below function gets executed
def game(event,x,y,flags,param):
   
    global pscore,cscore,g
   
    if event==cv2.EVENT_LBUTTONDBLCLK:
        
        if x>=200 and x<=400 and y>=450 and y<=500:
            img[150:600,0:600]=(0,0,0)
            
            y1=random.randint(1,3)   #random number generation,decides which gesture computer has to pick
         
            if y1==1:
                img[0:150,0:150]=rock
                
            elif y1==2:
                img[0:150,0:150]=paper
                
            elif y1==3:
                img[0:150,0:150]=scissor
                
                
            p=player(frame)  #get the player's gesture
           #decide who get's the score
            if y1!=p:
                if (y1==1 and p==3) or(y1==2 and p==1) or (y1==3 and p==2):
                    cscore=cscore+1
                
                elif (y1==1 and p==2) or(y1==2 and p==3) or (y1==3 and p==1) :
                    pscore=pscore+1
                    
            score(10,500,cscore)  #update the scores a
            score(410,500,pscore)
            
            
            cv2.putText(img,"Bot score:"+str(cscore),(0,550),4,1,(100,255,100),2)
            cv2.putText(img,"score:"+str(pscore),(410,550),4,1,(100,255,100),2)
            img[155:195,0:160,]=imgsList[y1-1]
            img[510:550,220:380,]=imgsList[p-1]
            if(pscore==3 or cscore==3):
                g=True
            
             
def score(x,y,score_obtained):
    global pscore,cscore
    cv2.rectangle(img,(x,y),(x+(60*score_obtained),y+30),(0,255,0),-1)
    
    

            
            
    
img=np.zeros((600,600,3),np.uint8) 
cv2.rectangle(img,(10,500),(190,530),(255,255,255),2)
cv2.rectangle(img,(410,500),(590,530),(255,255,255),2)
cap=cv2.VideoCapture(0)

rock=cv2.imread('rock.png')
rock=cv2.resize(rock,(150,150))

paper=cv2.imread('paper.jpg')
paper=cv2.resize(paper,(150,150))

play=cv2.imread('play.png')
play=cv2.resize(play,(160,40))

scissor=cv2.imread('scissor.jpg')
scissor=cv2.resize(scissor,(150,150))


flag=0


while(True):
   
    if(g==True): #stop the game as soon as any of the player reaches score 3
        flag=1
        break
        
            
    ret,frame=cap.read()
    frame=cv2.resize(frame,(600,600))
    frame[450:490,220:380]=play
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',game)
    frame=cv2.bitwise_or(frame,img) 
    cv2.imshow('image',frame)
    cv2.imshow('im',img)
    
    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
#displaying the winner
if(flag):
    img[:,:]=(100,100,100)
    cv2.putText(img,"Game over",(150,300),4,2,(255,200,100),2)
    if(pscore==3):
        cv2.putText(img,"You win",(180,360),4,2,(255,200,100),2)
    elif(cscore==3):
        cv2.putText(img,"You lose",(180,360),4,2,(255,200,100),2)
    cv2.putText(img,"Bot score:"+str(cscore),(200,400),4,1,(0,0,0),2)
    cv2.putText(img,"Your score:"+str(pscore),(200,430),4,1,(0,0,0),2)
    while(flag):
        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF==27:
            break
cv2.destroyAllWindows()