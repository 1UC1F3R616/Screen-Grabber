# -*- coding:utf-8 -*-

import pyfiglet
import time
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener
from ctypes import windll


user32 = windll.user32
user32.SetProcessDPIAware()

def help_manual():
    print('\n\nScreenshots are stored at place where this application is present.')
    print('\nSimply hit left-shift and screen shot will be saved.\n\n')

def welcome():
    print(pyfiglet.figlet_format('Screen Graber', font='graffiti'))
    print('\n-Kush')

welcome()
help_manual()

count=1
def count_update():
    global count
    print('Screenshots Grabbed: '+str(count), end='\r')
    count+=1

def grab_show():
    im=ImageGrab.grab(bbox=None)
    im.save(str(time.time()) + '.jpg')

def on_press(key):
    pass

def on_release(key):
        if key == Key.shift :
            grab_show()
            count_update()
            
keyboard = Controller()

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

