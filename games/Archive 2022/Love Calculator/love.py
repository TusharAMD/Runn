def getper():
    list=[]
    for i in range(50,101):
        list.append(i)
    return random.choice(list)
import time
import random
x=1
while(x!=0):
    print("********WELCOME TO THE LOVE CALCULATOR********")
    #print("")
    print("")
    print("Enter your name and your Partner's name to find your love percentage ")
    name=input("Enter your name :    ")
    name2=input("Enter your Partner name :    ")
    time.sleep(1)
    print("Your calculations are being processed please wait for few seconds ...")
    time.sleep(3)
    p=getper()
    if(p==100):
        print("OMGGGG!!! your crush loves you soo much your your love is ",p,"%")
    if(p==50):
        print("You have to improve your love")
    else:
        print("Your love percent is  ",p,"%")
    print()
    print()
    print("Do you want to try it again ")
    print("if yes press 1      ")
    print("if no press 0       ")
    x=int(input()) 
