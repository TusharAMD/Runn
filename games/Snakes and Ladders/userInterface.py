import random
from tkinter import *
from diceMove import dice
import time


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


Canvas.create_circle = _create_circle


class MatchPosition():
    def find_snake_or_ladder(self, block, turn, position):
        x = 35 * (turn >= 3)
        y = (turn % 3) * 35
        if block == 3:
            return 305 + x, 150 + y, 22
        elif block == 5:
            return 545 + x, 390 + y, 8
        elif block == 11:
            return 185 + x, 30 + y, 26
        elif block == 20:
            return 545 + x, 30 + y, 29
        elif block == 17:
            return 425 + x, 510 + y, 4
        elif (block == 19):
            return 665 + x, 390 + y, 7
        elif (block == 21):
            return 425 + x, 390 + y, 9
        elif (block == 27):
            return 65 + x, 510 + y, 1
        else:
            return position[0], position[1], block


class Display(object):
    def __init__(self, master, img):

        # Create board of snake and ladder
        canvas_width = 850
        canvas_height = 600
        self.color = ["#FFF", "#F00", "#0F0", "#00F", "#FF0", "#0FF"]
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="brown")
        self.canvas.grid(padx=0, pady=0)
        self.canvas.create_image(360, 300, anchor=CENTER, image=img)

        self.x = 65
        self.y = 510
        self.m = []
        self.num_player = "Players"
        self.player = []
        self.position = []
        self.i = 0
        self.block = []
        self.move = 1
        self.turn = 0

        # Drop Menu
        OPTIONS = ["Players", "2", "3", "4", "5", "6"]
        variable = StringVar(master)
        variable.set(OPTIONS[0])  # default value
        w = OptionMenu(self.canvas, variable, *OPTIONS, command=self.get_choice)
        w.pack()
        w.place(x=740, y=225)
        w.config(font=('calibri', (10)), bg='white', width=5)

        # Start Game
        self.startGame = Button(self.canvas, text="Start", background='white', command=self.startGame,
                                font=("Helvetica"))
        self.startGame.place(x=770, y=400)

    def startGame(self):
        if (self.num_player == "Players"):
            pass
        else:
            # Dice
            # Screen
            self.canvas.create_rectangle(810, 150, 760, 100, fill='white', outline='black')
            self.canvas.pack(fill=BOTH, expand=1)
            # Button
            self.diceRoll = Button(self.canvas, text="Roll", background='white',
                                   command=self.gamePlay, font=("Helvetica"))
            self.num_player = int(self.num_player)
            self.diceRoll.place(x=770, y=165)
            self.create_peice()
            self.startGame.place(x=-30, y=-30)

    def get_choice(self, value):
        self.num_player = value

    def diceMove(self, position, turn):
        move = dice()
        # move = 1
        # Print Dice Value to screen
        dice_value = Label(self.canvas, text=str(move),
                           background='white', font=("Helvetica", 25))
        dice_value.pack()
        dice_value.place(x=775, y=105)

        self.x, self.y = position[0], position[1]
        if (move + self.block[turn] > 30):
            return [self.x, self.y]

        self.move = move
        self.block[turn] += move

        self.canvas.delete(self.player[turn])
        self.peices(move, turn)

        return [self.x, self.y]

    def peices(self, move, turn):
        # Starting value of and x and y should be 120 and 120
        # In create_circle initial value of x and y should be 100 and 550
        # To reach to the last block x should be 5*x and y should be 4*y
        # X should be added to value and Y should be subtracted
        # 5x120=600 and 4*120=480
        # m is the constant that tells which side to move i.e. left to right or right to left
        for i in range(move, 0, -1):
            self.x = self.x + 120 * self.m[turn]

            if (self.x > 665 and turn < 3):
                self.y = self.y - 120
                self.x = 665
                self.m[turn] = -1
            elif (self.x > 700 and turn >= 3):
                self.y = self.y - 120
                self.x = 700
                self.m[turn] = -1
            if (self.x < 65 and turn < 3):
                self.x = 65
                self.y -= 120
                self.m[turn] = 1
            elif (self.x < 100 and turn >= 3):
                self.x = 100
                self.y -= 120
                self.m[turn] = 1
            if (self.y < 30):
                self.y = 30

            # Code For the Animation of piece
            self.canvas.delete(self.player[turn])
            self.player[turn] = self.canvas.create_circle(self.x, self.y, 15, fill=self.color[turn],
                                                          outline=self.color[turn])
            self.canvas.update()
            time.sleep(0.25)

        print(self.x, self.y, self.block[turn])
        self.x, self.y, self.block[turn] = MatchPosition().find_snake_or_ladder(self.block[turn], turn,
                                                                                [self.x, self.y])

        if (any(self.y == ai for ai in [390, 425, 460, 150, 185, 220])):
            self.m[turn] = -1
        else:
            self.m[turn] = 1
        print(self.x, self.y, self.block[turn])
        self.canvas.delete(self.player[turn])
        self.player[turn] = self.canvas.create_circle(self.x, self.y, 15, fill=self.color[turn], outline="")

    def create_peice(self):
        for i in range(int(self.num_player)):
            if (i == 3):
                self.x += 35
                self.y -= 105
            self.player.append(self.canvas.create_circle(self.x, self.y, 15, fill=self.color[i], outline=""))
            self.position.append([self.x, self.y])
            self.m.append(1)
            self.block.append(1)
            self.y += 35

    def gamePlay(self):
        if (self.move == 6):
            turn = self.turn
        else:
            turn = self.i % self.num_player
            self.i += 1
            self.turn = turn
        self.position[turn] = self.diceMove(self.position[turn], turn)
        if (self.block[self.turn] >= 30):
            self.diceRoll.place(x=-30, y=-30)
            print("Won", self.turn + 1)
            top = Toplevel()
            top.title("Snakes and Ladders")
            message = "Player " + str(self.turn + 1) + " Won"
            msg = Message(top, text=message)
            top.geometry("%dx%d%+d%+d" % (100, 100, 250, 125))
            msg.pack()
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
