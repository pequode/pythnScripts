#genneral Program to Repeat mouse movements, like an autoclicker
import pynput
import time
from pynput.mouse import Button,Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as cont
# this whole program is a wrapper for the click methods in pynput
mouse = Controller()
keyboard = cont()
delayM = 0.12
delayK = 0.13
def getMPosCurrent():
    print(mouse.position)
# used to make clicks harded to detect
def clickHere(x,y):
    mouse.position = (x,y)
    time.sleep(delayM)
    mouse.click(Button.left,1)
def clickHereN(x,y,n):
    mouse.position = (Hx,y)
    time.sleep(delayM)
    mouse.click(Button.left,n)
def rClickHere(x,y):
    mouse.position = (x,y)
    time.sleep(delayM)
    mouse.click(Button.right,1)
def rClickHereN(x,y,n):
    mouse.position = (x,y)
    time.sleep(delayM)
    mouse.click(Button.left,n)
def scrollThisAmt(y):
    mouse.scroll(0,-y)
def scrollThisAmtX(x,y):
    mouse.scroll(x,-y)
def typeThis(stri):
    for char in stri:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(delayK)
def typeThisN(stri,n):
    for i in range(0,n):
        for char in stri:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(delayK)
#this is ust a test             
clickHere(1200,200)
typeThis("print(\"Hello World!\")")
