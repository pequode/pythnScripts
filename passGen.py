#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# program to create randomly generated passwoerds
import random as rd
passLength = 16
string = ""
def numShift(num):
    #48-57 is nums 9
    #33-38 special chars 5
    #64-90 Capitals 26
    #97-122 lower case 25
    if(num < 5):
        return num+33
    elif(num < 5+9):
        return num-5+48
    elif(num < 5+9+26):
        return num-5-9+64
    elif(num < 5+9+26+25):
        return num-5-9-26+97
    else:
        return 33
for i in range(passLength):
    char = chr(numShift(rd.randint(0,65)))
    string = string + char  # 48 -175
print (string)
print (len(string))
