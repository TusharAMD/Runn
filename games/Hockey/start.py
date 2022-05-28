import sys, random

if sys.version_info.major > 2:
    import tkinter as tk
else:
    import Tkinter as tk
RED, BLACK, WHITE, DARK_RED, BLUE = "red", "black", "white", "dark red", "blue"
ZERO = 2 #for edges.
LOWER, UPPER = "lower", "upper"
HOME, AWAY = "Top", "Bottom"
#Should ALWAYS make a copy of START_SCORE before using it - START_SCORE.copy().
START_SCORE = {HOME: 0, AWAY: 0}
MAX_SCORE = 7 #Winning score.
SPEED = 20 #milliseconds between frame update.
FONT = "ms 50"
MAX_SPEED, PADDLE_SPEED = 15, 15

#### METHODS ####

def str_dict(dic):
    """ Returns a string version of score dictionary - dic """
    return "%s: %d, %s: %d" % (HOME, dic[HOME], AWAY, dic[AWAY])
    
def rand():
    """
    Picks a random tuple to return out of:
    (1, 1), (1, -1), (-1, 1), (-1, -1)
    """
    return random.choice(((1, 1), (1, -1), (-1, 1), (-1, -1))) 
    
#### OBJECT DEFINITIONS ####
        
class Equitment(object):
    """
    Parent class of Puck and Paddle.
    canvas: tk.Canvas object.
    width: int, radius of object.
    position: tuple, initial position (x, y).
    color: string, color of object.
    """
    def __init__(self, canvas, width, position, color):
        self.can, self.w = canvas, width
        self.x, self.y = position
        
        self.Object = self.can.create_oval(self.x-self.w, self.y-self.w, 
                                    self.x+self.w, self.y+self.w, fill=color)
    def update(self, position):
        self.x, self.y = position
        self.can.coords(self.Object, self.x-self.w, self.y-self.w,
                                     self.x+self.w, self.y+self.w)
    def __eq__(self, other):
        overlapping = self.can.find_overlapping(self.x-self.w, self.y-self.w,
                                                self.x+self.w, self.y+self.w)
        return other.get_object() in overlapping
        
    def get_width(self):
        return self.w
    def get_position(self):
        return self.x, self.y
    def get_object(self):
        return self.Object
        
class PuckManager(Equitment):
    """
    A black instance of Equitment.
    canvas: tk.Canvas object.
    width: int, radius of puck.
    position: tuple, initial position (x, y).
    """
    def __init__(self, canvas, width, position):
        Equitment.__init__(self, canvas, width, position, BLACK)
        
class Paddle(Equitment):
    """
    A red instance of Equitment with an extra drawing (handle).
    canvas: tk.Canvas object.
    width: int, radius of paddle.
    position: tuple, initial position (x, y).
    """  
    def __init__(self, canvas, width, position):
        Equitment.__init__(self, canvas, width, position, RED)
        self.handle = self.can.create_oval(self.x-self.w/2, self.y-self.w/2,
                                self.x+self.w/2, self.y+self.w/2, fill=DARK_RED)
    def update(self, position):
        Equitment.update(self, position)
        self.can.coords(self.handle, self.x-self.w/2, self.y-self.w/2,
                                   self.x+self.w/2, self.y+self.w/2)
                                   
class Background(object):
    """
    canvas: tk.Canvas object.
    screen: tuple, screen size (w, h).
    goal_w: int, width of the goal.
    """
    def __init__(self, canvas, screen, goal_w):
        self.can, self.goal_w = canvas, goal_w     
        self.w, self.h = screen
        
        self.draw_bg()
    
    def draw_bg(self):
        self.can.config(bg=WHITE, width=self.w, height=self.h)
        #middle circle
        d = self.goal_w/4
        self.can.create_oval(self.w/2-d, self.h/2-d, self.w/2+d, self.h/2+d, 
                                                     fill=WHITE, outline=BLUE)
        self.can.create_line(ZERO, self.h/2, self.w, self.h/2, fill=BLUE)#middle
        self.can.create_line(ZERO, ZERO, ZERO, self.h, fill=BLUE) #left
        self.can.create_line(self.w, ZERO, self.w, self.h, fill=BLUE) #right
        #top
        self.can.create_line(ZERO, ZERO, self.w/2-self.goal_w/2, ZERO, 
                                                                     fill=BLUE)
        self.can.create_line(self.w/2+self.goal_w/2, ZERO, self.w, ZERO, 
                                                                     fill=BLUE)
        #bottom
        self.can.create_line(ZERO, self.h, self.w/2-self.goal_w/2, self.h, 
                                                                     fill=BLUE)
        self.can.create_line(self.w/2+self.goal_w/2, self.h, self.w, self.h, 
                                                                     fill=BLUE)
                                                                     
    def is_position_valid(self, position, width, constraint=None):
        x, y = position
        #if puck is in goal, let it keep going in.
        if constraint == None and self.is_in_goal(position, width):
            return True
        elif (x - width < ZERO or x + width > self.w or 
            y - width < ZERO or y + width > self.h):
            return False
        elif constraint == LOWER:
            return y - width > self.h/2
        elif constraint == UPPER:
            return y + width < self.h/2
        else:
            return True    

    def is_in_goal(self, position, width):
        x, y = position
        if (y - width <= ZERO and x - width > self.w/2 - self.goal_w/2 and 
                                    x + width < self.w/2 + self.goal_w/2):
            return HOME
        elif (y + width >= self.h and x - width > self.w/2 - self.goal_w/2 and 
                                        x + width < self.w/2 + self.goal_w/2):
            return AWAY
        else:
            return False
            
    def get_screen(self):
        return self.w, self.h   
    def get_goal_w(self):
        return self.goal_w
        
class Puck(object):
    """
    canvas: tk.Canvas object.
    background: Background object.
    """
    def __init__(self, canvas, background):
        self.background = background
        self.screen = self.background.get_screen()
        self.x, self.y = self.screen[0]/2, self.screen[1]/2
        self.can, self.w = canvas, self.background.get_goal_w()/12
        c, d = rand() #generate psuedorandom directions.
        self.vx, self.vy = 4*c, 6*d
        self.a = .99 #friction
        self.cushion = self.w*0.25
        
        self.puck = PuckManager(canvas, self.w, (self.y, self.x))
        
    def update(self):
        #hockey table
        if self.vx > 0.25: self.vx *= self.a
        if self.vy > 0.25: self.vy *= self.a
        
        x, y = self.x + self.vx, self.y + self.vy
        if not self.background.is_position_valid((x, y), self.w):
            if x - self.w < ZERO or x + self.w > self.screen[0]:
                self.vx *= -1
            if y - self.w < ZERO or y + self.w > self.screen[1]:
                self.vy *= -1
            x, y = self.x+self.vx, self.y+self.vy
            
        self.x, self.y = x, y
        self.puck.update((self.x, self.y))

    def hit(self, paddle, moving):
        x, y = paddle.get_position()

        if moving:        
            if (x > self.x - self.cushion and x < self.x + self.cushion or 
                                                    abs(self.vx) > MAX_SPEED):
                xpower = 1
            else:
                xpower = 5 if self.vx < 2 else 2
            if (y > self.y - self.cushion and y < self.y + self.cushion or 
                                                    abs(self.vy) > MAX_SPEED):
                ypower = 1
            else:
                ypower = 5 if self.vy < 2 else 2
        else:
            xpower, ypower = 1, 1
            
        if self.x + self.cushion < x:
            xpower *= -1
        if self.y + self.cushion < y:
            ypower *= -1
        
        self.vx = abs(self.vx)*xpower
        self.vy = abs(self.vy)*ypower
    
    def __eq__(self, other):
        return other == self.puck
    def in_goal(self):
        return self.background.is_in_goal((self.x, self.y), self.w)

class Player(object):
    """
    master: tk.Tk object.
    canvas: tk.Canvas object.
    background: Background object.
    puck: Puck object.
    constraint: UPPER or LOWER (can be None).
    """
    def __init__(self, master, canvas, background, puck, constraint):
        self.puck, self.background = puck, background
        self.constraint, self.v = constraint, PADDLE_SPEED
        screen = self.background.get_screen()
        self.x = screen[0]/2
        self.y = 60 if self.constraint == UPPER else screen[1] - 50

        self.paddle = Paddle(canvas, self.background.get_goal_w()/7,
                                                            (self.x, self.y))
        self.up, self.down, self.left, self.right = False, False, False, False
        
        if self.constraint == LOWER:
            master.bind('<Up>', self.MoveUp)
            master.bind('<Down>', self.MoveDown)
            master.bind('<KeyRelease-Up>', self.UpRelease)
            master.bind('<KeyRelease-Down>', self.DownRelease)
            master.bind('<Right>', self.MoveRight)
            master.bind('<Left>', self.MoveLeft)
            master.bind('<KeyRelease-Right>', self.RightRelease)
            master.bind('<KeyRelease-Left>', self.LeftRelease)
        else:
            master.bind('<w>', self.MoveUp)
            master.bind('<s>', self.MoveDown)
            master.bind('<KeyRelease-w>', self.UpRelease)
            master.bind('<KeyRelease-s>', self.DownRelease)
            master.bind('<d>', self.MoveRight)
            master.bind('<a>', self.MoveLeft)
            master.bind('<KeyRelease-d>', self.RightRelease)
            master.bind('<KeyRelease-a>', self.LeftRelease)
        
    def update(self):
        x, y = self.x, self.y
        
        if self.up: y = self.y - self.v
        if self.down: y = self.y + self.v
        if self.left: x = self.x - self.v
        if self.right: x = self.x + self.v
        
        if self.background.is_position_valid((x, y), 
                                      self.paddle.get_width(), self.constraint):
            self.x, self.y = x, y
            self.paddle.update((self.x, self.y))
        if self.puck == self.paddle:
            moving = any((self.up, self.down, self.left, self.right))
            self.puck.hit(self.paddle, moving)
    
    def MoveUp(self, callback=False):
        self.up = True
    def MoveDown(self, callback=False):
        self.down = True
    def MoveLeft(self, callback=False):
        self.left = True
    def MoveRight(self, callback=False):
        self.right = True
    def UpRelease(self, callback=False):
        self.up = False
    def DownRelease(self, callback=False):
        self.down = False
    def LeftRelease(self, callback=False):
        self.left = False
    def RightRelease(self, callback=False):
        self.right = False
        
class Home(object):
    """
    Game Manager.
    master: tk.Tk object.
    screen: tuple, screen size (w, h).
    score: dict.
    """
    def __init__(self, master, screen, score=START_SCORE.copy()):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.can = tk.Canvas(self.frame)
        self.can.pack()
        #goal width = 1/3 of screen width
        background = Background(self.can, screen, screen[0]*0.33)
        self.puck = Puck(self.can, background)
        self.p1 = Player(master, self.can, background, self.puck, UPPER)
        self.p2 = Player(master, self.can, background, self.puck, LOWER)
        
        master.bind("<Return>", self.reset)
        master.bind("<r>", self.reset)
        
        master.title(str_dict(score))
        
        self.master, self.screen, self.score = master, screen, score
        
        self.update()
        
    def reset(self, callback=False):
        """ <Return> or <r> key. """
        if callback.keycode == 82: #r key resets score.
            self.score = START_SCORE.copy()
        self.frame.destroy()
        self.__init__(self.master, self.screen, self.score)
        
    def update(self):
        self.puck.update()
        self.p1.update()
        self.p2.update()
        if not self.puck.in_goal():
            self.frame.after(SPEED, self.update) 
        else:
            winner = HOME if self.puck.in_goal() == AWAY else AWAY
            self.update_score(winner)
            
    def update_score(self, winner):
        self.score[winner] += 1
        self.master.title(str_dict(self.score))
        if self.score[winner] == MAX_SCORE:
            self.frame.bell()
            self.can.create_text(self.screen[0]/2, self.screen[1]/2, font=FONT,
                                                     text="%s wins!" % winner)
            self.score = START_SCORE.copy()
        else:
            self.can.create_text(self.screen[0]/2, self.screen[1]/2, font=FONT,
                                                 text="Point for %s" % winner)
                                                 
def play(screen):
    """ screen: tuple, screen size (w, h). """
    root = tk.Tk()
#    root.state("zoomed")
#    root.resizable(0, 0)
    Home(root, screen)
    #root.eval('tk::PlaceWindow %s center' %root.winfo_pathname(root.winfo_id()))
    root.mainloop()
            
if __name__ == "__main__":
    """ Choose screen size """  
    screen = 700, 760
    
    play(screen)