# Program to randomly move your mouse pointer in your screen

import pyautogui
import tkinter as tk
import random
import time

if __name__ == '__main__':

    mouseSpeed = 1 # seconds

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width, screen_height)
    print('Program Started: \n Press CTRL + C to Stop the program')
    while True:
        pyautogui.moveTo(random.randint(0,screen_width), random.randint(0,screen_height),2)
        time.sleep(mouseSpeed)
    print('End of the Program')
