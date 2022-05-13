from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from random import randint
root = Tk()
root.attributes("-fullscreen", False)
root.title('Snake And Ladder')
root.configure(bg='Black')
root.iconbitmap(None)
root.geometry("343x400")
root.resizable(height = 0, width = 0)
def endIt():return None
def diceOn():
    l,s,prev1,prev2=False,False,1,1
    dicef=''
    global now,q,temp,count6,p1coord,p2coord
    q=randint(1,6)
    tempq=int(q)
    if (q+p1coord[2] in ladder[0]) and now==1:
        m=ladder[0].index(q+p1coord[2])
        q=ladder[1][m]-1
        prev1=p1coord[2]
        p1coord=[9,315,1]
        l=True
    elif (q+p2coord[2] in ladder[0]) and now==2:
        m=ladder[0].index(q+p2coord[2])
        q=ladder[1][m]-1
        prev2=p2coord[2]
        p2coord=[9,315,1]
        l=True
    elif (q+p1coord[2] in snake[0]) and now==1:
        m=snake[0].index(q+p1coord[2])
        q=snake[1][m]-1
        prev1=p1coord[2]
        p1coord=[9,315,1]
        s=True
    elif (q+p2coord[2] in snake[0]) and now==2:
        m=snake[0].index(q+p2coord[2])
        q=snake[1][m]-1
        prev2=p2coord[2]
        p2coord=[9,315,1]
        s=True
    else:
        if now==1:prev1=p1coord[2]
        elif now==2:prev2=p2coord[2]
        if q+p1coord[2]>100 and now==1:
            now=2
            label['text']="P1, U can't move"
            return True
        if q+p2coord[2]>100 and now==2:
            now=1
            label['text']="P2, U can't move"
            return True
        if temp2[0]!=None:temp2[1]=q
        if q==6:count6+=1
        if count6==1:
            temp2[0]=q
            if now==1:temp[0],temp[1],temp[2]=p1coord[0],p1coord[1],p1coord[2]
            if now==2:temp[0],temp[1],temp[2]=p2coord[0],p2coord[1],p2coord[2]
        elif count6==3:
            if temp2[1]!=None:temp2[2]=q
            if (temp2[0]==6 and temp2[1]==6) and temp2[2]==6:
                if now==1:p1coord[0],p1coord[1],p1coord[2]=temp[0],temp[1],temp[2]
                if now==2:p2coord[0],p2coord[1],p2coord[2]=temp[0],temp[1],temp[2]
                count6=0
                temp2[0],temp2[1],temp2[2]=None,None,None
                eval('p'+str(now)+'.place(x='+str(p1coord[0])+',y='+str(p1coord[1])+',width=15, height=15)')
                return True
            else:
                count6=0
                temp2[0],temp2[1],temp2[2]=None,None,None
    if q==1 or tempq==1:dicef='⚀'
    elif q==2 or tempq==2:dicef='⚁'
    elif q==3 or tempq==3:dicef='⚂'
    elif q==4 or tempq==4:dicef='⚃'
    elif q==5 or tempq==5:dicef='⚄'
    elif q==6 or tempq==6:dicef='⚅'
    dice['text'] = dicef
    for i in range(q):
        if now==1:
            if p1coord[2] in range(11,20) or p1coord[2] in range(31,40) or p1coord[2] in range(51,60) or p1coord[2] in range(71,80) or p1coord[2] in range(91,100):p1coord[0]-=35
            else:p1coord[0]+=35
            if p1coord[2]%10==0 and p1coord[2]!=100:
                p1coord[1]-=33
                p1coord[0]-=35
            p1coord[2]+=1
        elif now==2:
            if p2coord[2] in range(11,20) or p2coord[2] in range(31,40) or p2coord[2] in range(51,60) or p2coord[2] in range(71,80) or p2coord[2] in range(91,100):p2coord[0]-=35
            else:p2coord[0]+=35
            if p2coord[2]%10==0 and p2coord[2]!=100:
                p2coord[1]-=33
                p2coord[0]-=35
            p2coord[2]+=1
        p1.place(x=p1coord[0],y=p1coord[1],width=15, height=15)
        p2.place(x=p2coord[0],y=p2coord[1],width=15, height=15)
    if now==1:
        if l==True:label['text']='P1 - From '+str(prev1)+' to '+str(p1coord[2])+' Ladder'
        elif s==True:label['text']='P1 - From '+str(prev1)+' to '+str(p1coord[2])+' Snake'
        else:label['text']='P1 - From '+str(prev1)+' to '+str(p1coord[2])
    elif now==2:
        if l==True:label['text']='P2 - From '+str(prev2)+' to '+str(p2coord[2])+' Ladder'
        elif s==True:label['text']='P2 - From '+str(prev2)+' to '+str(p2coord[2])+' Snake'
        else:label['text']='P2 - From '+str(prev2)+' to '+str(p2coord[2])

    if (now==1 and q!=6)and tempq!=6:now=2
    elif (now==2 and q!=6)and tempq!=6:now=1
    q=randint(1,6)
    if p1coord[2]==100:
        label['text']='P1 Won!!!'
        dice['command']=endIt
    if p2coord[2]==100:
        label['text']='P2 Won!!!'
        dice['command']=endIt
    if p1coord[2]==p2coord[2]:
        p1.place(x=p1coord[0]-5,y=p1coord[1]-5,width=15, height=15)
        p2.place(x=p2coord[0],y=p2coord[1],width=15, height=15)

#Button
temp=[None,None,None]
temp2=[None,None,None]
count6=0
now=1
q=0
ladder=[[2,7,8,15,21,28,36,51,71,78,87],[38,14,31,26,42,84,44,67,91,98,94]]
snake=[[99,95,92,74,64,62,49,46,16],[80,75,88,53,60,19,11,25,6]]

photo = PhotoImage(file="./img/Board.png")
label = Label(root,image=photo)
label.place(x=0,y=0)

p1 = Label(root,bg='cyan',text='P1',fg='black')
p1.place(x=10,y=305,width=15, height=15)
p1coord=[9,315,1]

p2 = Label(root,bg='lime',text='P2',borderwidth=5)
p2.place(x=15,y=315,width=15, height=15)
p2coord=[9,315,1]

dice = Button(root,text='+',fg = 'White',bg='Black',activebackground='black',borderwidth=0,command=diceOn)
dice['font'] = font.Font(size=50)
dice.place(x=5,y=350,width=50, height=35)

label = Label(root,text='',fg = 'White',bg='Black')
label['font'] = font.Font(size=14)
label.place(x=110,y=370)

root.mainloop()
