''' this is the TpObjClass
this class is in charge of tracking individual points of a specphic color
it is a rough draft
@author George Kent-Scheller
@version 07132018 (12:53AM-
'''
import numpy as np
import cv2
import scipy
import matplotlib
import os
from point import Point

class tpObj:
   
    
    # this creates a camera obj for the prg
    goPro = cv2.VideoCapture(0)
    # this gives input for the desired size of the image given by width. it is user input to deterime track quality
    desImgSzWd = 250

    # this gets the height of the image as a float value
    width = goPro.get(3) 
    height = goPro.get(4)
    sizeratio = (width * 1.0) /height
    desImgSzHt = (int)(desImgSzWd/sizeratio)
    # this creats a font for feedback on the img
    font=cv2.FONT_HERSHEY_SIMPLEX
    
    # this is a definition of center definitions of color
    blue = np.array([240,168,148])#0
    green = np.array([120,168,148])#1
    red = np.array([0,168,148])#2
    yellow = np.array([60,168,148])#3
    purple = np.array([300,168,148])#4
    orenge = np.array([30,168,148])#5
    alpha = np.array([0,0,255])#6
    nullPointHa = Point(0,0)
    colors = np.array([blue,green,red,yellow,purple,orenge,alpha])
    colorNames = np.array(["Blue","Green","Red","Yellow","Purple","Orenge","Alpha"])
    pColorName = "Bro No Color!"
    lowKR = 3
    HighKR = 10
    #just for george testing
    
    # this records the inital position & the color being tracked 
    def __init__(self,color):# color is an int # 1-6
        self.initialPos = Point(0,0)
        self.pColor = colors[color]
        self.pColorName = colorNames[color]
        self.cTolerance = 30
        self.pTolerance = 100
        self.recentPos = np.array([nullPointHa,nullPointHa])
        self.expectedPos = nullPointHa
        self.internalCTollMeth()
        self.KOPVAL = 3
        self.KCLVAL = 10
        #this defines the kenal used in noise reduction. the lower the kernal value the more precise but more noise
        self.kernalOP=np.ones((KOPVAL,KOPVAL))
        self.kernalCL=np.ones((KCLVAL,KCLVAL))
        '''
    def __init__(self,pnt,color,cToll,pToll):# color is an int # 1-6
        self.initialPos = pnt
        self.pColor = colors[color]
        self.pColorName = colorNames[color]
        self.cTolerance = cToll
        self.pTolerance = pToll
        self.recentPos = np.array([nullPointHa,nullPointHa])
        self.expectedPos = nullPointHa
        self.internalCTollMeth()
        #need to decide if it needs to be a perameter
        self.KOPVAL = lowKR
        self.KCLVAL = HighKR
        #this defines the kenal used in noise reduction. the lower the kernal value the more precise but more noise
        self.kernalOP=np.ones((KOPVAL,KOPVAL))
        self.kernalCL=np.ones((KCLVAL,KCLVAL))
'''

    def internalCTollMeth (self):
        self.lowerCBound = self.pColor
        self.lowerCBound[0] -= self.cTolerance
        self.lowerCBound[1] -= self.cTolerance
        self.lowerCBound[2] -= self.cTolerance
        self.upperCBound = self.pColor
        self.upperCBound[0] += self.cTolerance
        self.upperCBound[1] += self.cTolerance
        self.upperCBound[2] += self.cTolerance
    def aprox (self):
        # 0 is the most recent entry in the array
        self.expectedPos = recentPos[1].aproxT(recentPos[0])
    # this allows us to place a track for each point    
    def changeTrPosition(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.recentPos[1] = self.recentPos[0]
            self.recentPos[0] = Point(x,y)
            
    def checkTrPostion (self, ppoint):
        if self.recentPos[0].getDistanceBetween(ppoint) < pTolerance:
            self.recentPos[1] = self.recentPos[0]
            self.recentPos[0] = ppoint
        else:
            print("you messed up bro")
        
    def runTrack (self):
        while True:
            # this returns fps data that helps measure processing time
            fps = goPro.get(cv2.CAP_PROP_FPS)
            # this gets the current image on the camera
            ret,img = goPro.read()
            # this decrease the size of the image while maintaining the same aspect ratio
            img = cv2.resize(img,(desImgSzWd,desImgSzHt))

            # this converts the image into HSV scale
            imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

            #this creates a filter for our green stickers
            mask = cv2.inRange(imgHSV,lowerBoundGreen,upperBoundGreen)


            #this is noise reduction
            maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernalOP)
            maskClose= cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernalCL)

            #this is the tracking step
            maskFinal = maskClose
            j,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(img,conts,-1,(255,0,0),1)

            for i in range (len(conts)):
                x,y,w,h=cv2.boundingRect(conts[i])
                # this is where i check tr pos 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
                cv2.putText(img,str(i+1),(x,y+h),font,1,(0,255,255),2)
           
            #this provides an exit key
            if cv2.waitKey(2) == ord(' '):
                    cv2.destroyAllWindows()
                    break
            # this allows us to check for clicks
            cv2.setMouseCallback('check',draw_circle)
            # this creats a window with a string title and takes an image as a peramiter
            cv2.imshow("check",img)
            cv2.imshow("MaskwKernalCL",maskClose)
            cv2.waitKey(10)
        goPro.release()

    
    
    


  
        

h = tpObj(3)
print(h.pColor)
#always need self, even when refering to class variables // class methods run on every obj use @classmethod
    #def bla ( cls, peram):
                 
