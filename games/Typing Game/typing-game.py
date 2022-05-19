from words import words


def slider():
    global count, sliderwords
    text = 'Welcome to Typing Game'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150, slider)


def time():
    global timer, score, miss
    if timer > 11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer > 0:
        timer -= 1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000, time)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'
                                  .format(score, miss, score - miss))
        rr = messagebox.askretrycancel('Notification', 'Wanna Play Again!!!!')
        if rr == True:
            score = 0
            miss = 0
            timer = 60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)


def startgame(event):
    global score, miss
    if timer == 60:
        time()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get() == wordlabel['text']:
        score += 1
        scorelabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0, END)


from tkinter import *
import random
from tkinter import messagebox

###############################################
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='black')
root.title('Typing Game')
root.iconbitmap('logo.ico')

##############################################

score = 0
miss = 0
timer = 60
count = 0
sliderwords = ''

#################################################################
fontlabel = Label(root, text='', font=('airal', 25,
                                       'italic bold'), bg='black', fg='purple', width=40)
fontlabel.place(x=10, y=10)
slider()

startlabel = Label(root, text='Lets begin!!!', font=('airal', 30,
                                                     'italic bold'), bg='black', fg='white')
startlabel.place(x=275, y=50)

random.shuffle(words)
wordlabel = Label(root, text=words[0], font=('airal', 45,
                                             'italic bold'), bg='black', fg='green')
wordlabel.place(x=350, y=240)

scorelabel = Label(root, text='Your Score:', font=('arial', 25,
                                                   'italic bold'), bg='black', fg='red')
scorelabel.place(x=10, y=100)

scorelabelcount = Label(root, text=score, font=('arial', 25,
                                                'italic bold'), bg='black', fg='blue')
scorelabelcount.place(x=150, y=180)

timerlabel = Label(root, text='Time Left:', font=('arial', 25,
                                                  'italic bold'), bg='black', fg='red')
timerlabel.place(x=600, y=100)

timerlabelcount = Label(root, text=timer, font=('arial', 25,
                                                'italic bold'), bg='black', fg='blue')
timerlabelcount.place(x=600, y=180)

gameinstruction = Label(root, text='Type the Word and hit enter button',
                        font=('arial', 25, 'italic bold'), bg='black', fg='grey')
gameinstruction.place(x=150, y=500)

########################################################################

wordentry = Entry(root, font=('airal', 25, 'italic bold'), bd=10, justify='center')
wordentry.place(x=250, y=330)
wordentry.focus_set()

#################################################################
root.bind('<Return>', startgame)
root.mainloop()
