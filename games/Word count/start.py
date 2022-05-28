#Imports
import tkinter as tk
from tkinter import *
from collections import Counter

#Functions
def countWords(s):
    signos = [',', '.', ';', ':']
    cleanstr = ''
    for letra in s.lower():
        if letra in signos:
            cleanstr += ''
        else:
            cleanstr += letra
    strlist = cleanstr.split(' ')
    return dict(Counter(strlist))


def button_count():
    text = mainWindow.e2.get()

    count = countWords(text)
    myLabel = Label(root, text=count)
    myLabel.pack()


#Graphics
root = tk.Tk()
root.title("Count words")
root.geometry('400x400')

#Class Window
class Window:

    def __init__(self, root):
        self.root = root
        self.e2 = tk.StringVar()
        self.e = tk.Entry(root, textvariable=self.e2, width=35, borderwidth=5)
        self.e.pack()

        self.button = Button(root, text="Count words", command=button_count)
        self.button.pack()
        self.exit_button = Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()


if __name__ == '__main__':
    
    mainWindow = Window(root)

        
    

root.mainloop()