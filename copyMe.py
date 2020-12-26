# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# this is for creating bots
from pynput.mouse import Listener as ls
from pynput.mouse import Button as btt
from pynput.mouse import Controller as cnt 
from pynput.keyboard import Key,Controller
from pynput.keyboard import Listener as lsn
import logging 
import time 
import math
path = "C:/Users/George Kunt Scheller/Music/Various Artists/"
logging.basicConfig(filename=(path+"log.txt"),level=logging.DEBUG, format = '%(asctime)s: %(message)s')
keyboard = Controller() 
mouse = cnt()
PathToFile = "C:/Users/George Kunt Scheller/Music/Various Artists/log.txt"
cntrPressed = False
selecting = False
x1 = 0 
y1  = 0
'''
def on_move(x,y):
    global selecting
    distance  = ((x-x1)^2+(y-y1)^2)^(1.0/2)
    
    selecting = distance > 10
'''
def on_move(x, y):
    global selecting
    distance  = math.sqrt((x-x1)**2+(y-y1)**2)
    selecting = distance > 9
    pass
def on_click(x,y,button,pressed):
    global x1, y1,selecting
    if not pressed:
        fl = open(PathToFile,'a')
        if selecting:
            line="mm"+str(x1)+","+str(y1)+"\n"+"ms"+str(x)+","+str(y)+"\n"
        elif button == btt.left:
            line = "mm"+str(x)+","+str(y)+"\nmc\n"
        elif button == btt.right:
            line = "mm"+str(x)+","+str(y)+"\nmr\n"
        else:
            print ("invalid button" + str(button))
            line==""
        print (line),
        fl.write(line)
        fl.close()
    else:
        x1 = x
        y1 = y
        selecting = False 
    pass
def on_scroll(x,y,dx,dy):
    fl = open(PathToFile,'a')
    line = "mm"+str(x)+","+str(y)+"\nmo"+str(dx)+","+str(dy)+"\n"
    print (line),
    fl.write(line)
    fl.close()
    pass
def pressed(key):
    global cntrPressed
    fl = open(PathToFile,'a')
    line= ""
    if key == Key.ctrl_l:
        cntrPressed = True
        line = "k!\n"

    elif key == Key.shift_l:
        line = "k@\n"
        
    elif key == Key.alt_l :
        line = "k^\n"
    elif key == Key.esc:
        return False
    else:
        line = "k$"+str(key)[2]+"\n"
    print (line),
    fl.write(line)
    fl.close()
    pass
def reled(key):
     global cntrPressed
     if key == (key == Key.ctrl_l):
        cntrPressed = False
        pass
     if key == Key.esc:
        return False
    

def copy():
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    keyboard.release('c')
def find(string):
    keyboard.press(Key.ctrl_l)
    keyboard.press('f')
    keyboard.release(Key.ctrl_l)
    keyboard.release('f')
    for i in string:
        keyboard.press(i)
        keyboard.release(i)
        time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def findkey():
    keyboard.press(Key.ctrl_l)
    keyboard.press('f')
    keyboard.release(Key.ctrl_l)
    keyboard.release('f')
    paste()
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def paste():
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    keyboard.release('v')
    
def moveTo(x1,y1,devs): 
    x = mouse._position_get()[0]
    y = mouse._position_get()[1]
    dy = (y1-y)/devs
    dx = (x1-x)/devs
    print (str(x) + "," +str(y))
    for i in range(devs):
        mouse.move(dx,dy)
        time.sleep(0.1)
    mouse.position = (x1,y1)

def readInstructions():
    f = open("C:/Users/George Kunt Scheller/Music/Various Artists/log.txt",'r')
    ls = f.readlines()
    
    for line in ls:
        print (line),
        if line[0] == 'm':
            if line[1] == 'm':
                pointsstr = line[2:]
                print (pointsstr)
                numChange = pointsstr.find(',')
                x =int(pointsstr[:numChange])
                y = int (pointsstr[numChange+1:-1])
                moveTo(x,y,10)
            elif line[1] == 'c':
                mouse.click(btt.left,1)
                time.sleep(0.3)
            elif line[1] == 'r':
                mouse.click(btt.right,1)
                time.sleep(0.3)
            elif line[1] == 's':
                pointsstr = line[2:]
                numChange = pointsstr.find(',')
                x =int(pointsstr[:numChange])
                y = int (pointsstr[numChange+1:-1])
                mouse.press(btt.left)
                moveTo(x,y,5)
                mouse.release(btt.left)
                time.sleep(1)
            elif line[1] == 'o':
                pointsstr = line[2:]
                numChange = pointsstr.find(',')
                dx =int(pointsstr[:numChange])
                dy = int (pointsstr[numChange+1:-1])
                mouse.scroll(dx,dy)
                time.sleep(0.3)
        elif line[0] == 'k':
            if line[1] == '$':
                keyboard.press(str(line[2]))
                keyboard.release(str(line[2]))
                time.sleep(0.1)
            elif line[1] == '!':
                copy()
            elif line[1] == '@':
                paste()
            elif line[1] == '^':
                findkey()
        else:
            print("error invalid instructions")            
    f.close()
    
def recordSteps():
    f = open(PathToFile,"w")
    f.close()
    with ls(on_move=on_move, on_click = on_click, on_scroll=on_scroll) as listener: #on_move=on_move, 
        with lsn(on_press = pressed,  on_release=reled) as listener:
            listener.join()
recordSteps()
readInstructions()





































"""
moveTo(500,500,10)
mouse.click(btt.left,1)
moveTo(1045,590,10)
moveTo(700,590,10)
mouse.press(btt.left)
moveTo(900,590,10)
mouse.release(btt.left)
copy()
#time.sleep(10)
moveTo(400,30,3)
mouse.click(btt.left,1)
time.sleep(0.1)
findkey()   
#find("name")
moveTo(800,675,1)
mouse.click(810,675,3)

moveTo(1000,500,20)
time.sleep(10)
mouse.scroll(0,-25)
moveTo(1040,590,10)
moveTo(1045,590,10)
"""
