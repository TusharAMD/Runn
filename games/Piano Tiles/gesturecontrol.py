import random
import time
import cv2
import imutils
import keyboard
import numpy as np
import pyautogui
import pytesseract
import win32api
import win32con

positions = list(range(start, end, jump))

while True:
     if keyboard.is_pressed('esc'):
         break
    elif keyboard.is_pressed('s'):
         print("Started")
         prev = -1
         while keyboard.is_pressed('q') == False and keyboard.is_pressed('Q') == False:
             for pos, col in enumerate(positions):
                 if prev != pos and pyautogui.pixel(col, row - delay)[0] < 50:
                     actionClick(col, row)
                     prev = pos
                     break
 print("Finished")
