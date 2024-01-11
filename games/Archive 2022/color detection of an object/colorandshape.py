# from tkinter import image_names
import cv2
from cv2 import split
from cv2 import arcLength
import numpy as np
image=cv2.imread("D:/instagramphotos/test_image_2.png")
img_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

l_red=np.array([0, 50, 70])
u_red=np.array([9, 255, 255])

l_green=np.array([36,0,0])
u_green=np.array([86,255,255])

lower_blue = np.array([94, 80, 2]) 
upper_blue = np.array([126, 255, 255])

img_mask=cv2.inRange(img_hsv,l_red,u_red)
res_red=cv2.bitwise_and(image,image,mask=img_mask)
ctr_red,hierarchy=cv2.findContours(img_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

img_maskg=cv2.inRange(img_hsv,l_green,u_green)
res_green=cv2.bitwise_and(image,image,mask=img_maskg)
ctr_green,hierarchy=cv2.findContours(img_maskg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

img_maskb=cv2.inRange(img_hsv,lower_blue,upper_blue)
res_blue=cv2.bitwise_and(image,image,mask=img_maskb)
ctr_blue,hierarchy=cv2.findContours(img_maskb,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

font=cv2.FONT_HERSHEY_SIMPLEX

for cnt in ctr_red:
    # print(cnt,sep=" ")
    # print( len(cnt))
    approx=cv2.approxPolyDP(cnt,0.02*arcLength(cnt,True),True)
    cv2.drawContours(image,approx,-1,(0,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    # print(x,y,sep=" ")
    # print("  ",len(approx)," ")
    if(len(approx)==4):
        (x,y,w,h)=cv2.boundingRect(approx)
        if (float(w)/h==1):
          cv2.putText(image,'square',(x,y),font,1,(0,0,0),2)
        else:
            cv2.putText(image,'rectangle-red',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==3):
         cv2.putText(image,'triangle-red',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==5):
         cv2.putText(image,'pentagon-red',(x,y),font,1,(0,0,0),2) 
    elif(len(approx)==9):
         cv2.putText(image,'halfcircle-red',(x,y),font,1,(0,0,0),2) 
    else:
         cv2.putText(image,'circle-red',(x,y),font,1,(0,0,0),2)                     

for cnt in ctr_green:
    # print(cnt,sep=" ")
    # print( len(cnt))
    approx=cv2.approxPolyDP(cnt,0.02*arcLength(cnt,True),True)
    cv2.drawContours(image,approx,-1,(0,0,0),2)
    x=approx.ravel()[0]-200
    y=approx.ravel()[1]
    # print(x,y,sep=" ")
    # print("  ",len(approx)," ")
    if(len(approx)==4):
        (x,y,w,h)=cv2.boundingRect(approx)
        if (float(w)/h==1):
          cv2.putText(image,'square',(x,y),font,1,(0,0,0),2)
        else:
            cv2.putText(image,'rectangle-green',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==3):
         cv2.putText(image,'triangle-green',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==5):
         cv2.putText(image,'pentagon-green',(x,y),font,1,(0,0,0),2) 
    elif(len(approx)==9):
         cv2.putText(image,'halfcircle-green',(x,y),font,1,(0,0,0),2) 
    else:
         cv2.putText(image,'circle-green',(x,y),font,1,(0,0,0),2) 

for cnt in ctr_blue:
    # print(cnt,sep=" ")
    # print( len(cnt))
    approx=cv2.approxPolyDP(cnt,0.02*arcLength(cnt,True),True)
    cv2.drawContours(image,approx,-1,(0,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    # print(x,y,sep=" ")
    # print("  ",len(approx)," ")
    if(len(approx)==4):
        (x,y,w,h)=cv2.boundingRect(approx)
        if (float(w)/h==1):
          cv2.putText(image,'square',(x,y),font,1,(0,0,0),2)
        else:
            cv2.putText(image,'rectangle-blue',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==3):
         cv2.putText(image,'triangle-blue',(x,y),font,1,(0,0,0),2)
    elif(len(approx)==5):
         cv2.putText(image,'pentagon-blue',(x,y),font,1,(0,0,0),2) 
    elif(len(approx)==9):
         cv2.putText(image,'halfcircle-blue',(x,y),font,1,(0,0,0),2) 
    else:
         cv2.putText(image,'circle-blue',(x,y),font,1,(0,0,0),2) 


cv2.imshow("contours",image)

cv2.waitKey()

cv2.destroyAllWindows()