import random
from pprint import pprint
from functools import partial
from datetime import datetime

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter import messagebox

msg = 'Click a square, you get a number.\
That number is the number of how many mines are surrounding it.\
If you find the mine, you can open "unopened" squares around it, opening more areas.'