import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)


def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update


app = Tk()
app.title("Math For Kids")



app.geometry("240x300")
app.resizable(False, False)
start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="Submit", command=lambda: submt(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.39, rely=0.9)
app.mainloop()