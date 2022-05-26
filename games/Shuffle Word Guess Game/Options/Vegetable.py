from tkinter import *
from random import *
from tkinter import messagebox
import time

VEGETABLE_WORD = ['OTCRRA', 'OIRCCOBL', 'ROUFCWIALEL', 'RNOC', 'UCMUECRB', 'GGNALETP', 'EEGRN EREPPP', 'ECETTUL',
                  'OSMROSMUH', 'INNOO', 'OATPTO', 'UNPMIPK', 'RED EPEPPR', 'MOTTOA', 'ETEBTROO', 'EPAS', 'HIRSAD',
                  'CEBABAG', 'CLIHI', 'ICRGAL', 'WETSE OTPAOT', 'RERAOCDIN', ]
VEGETABLE_ANSWER = ['CARROT', 'BROCCOLI ', 'CAULIFLOWER ', 'CORN ', 'CUCUMBER ', 'EGGPLANT', 'GREEN PEPPER ',
                    'LETTUCE ', 'MUSHROOMS', 'ONION', 'POTATO', 'PUMPKIN ', 'RED PEPPER', 'TOMATO ', 'BEETROOT', 'PEAS',
                    'RADISH', 'CABBAGE', 'CHILI', 'GARLIC', 'SWEET POTATO', 'CORIANDER', ]

ran_num = randrange(0, (len(VEGETABLE_WORD)))
jumbled_rand_word = VEGETABLE_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(VEGETABLE_WORD)))
        word.configure(text=VEGETABLE_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == VEGETABLE_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(VEGETABLE_WORD)))
            word.configure(text=VEGETABLE_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=VEGETABLE_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Shuffle Word Guess Game")
    my_window.configure(background="#3a1978")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#3a1978',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#3a1978",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#3a1978",
        fg="#000000",
        font="Titillium  40 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#3a1978",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
