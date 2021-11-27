''' this was created as a test page to help
@author George Kent-Scheller Understand the
concepts behind OpenCV and CV in general.
@version 07112018.1(3PM-7:10PM),9:30AM-5.00 PM)'''

import numpy as np
import cv2
import scipy
import matplotlib
import os
# this was made possible by a tutorial from the following website: https://thecodacus.com/opencv-object-tracking-colour-detection-python
#this imports the camera
goPro = cv2.VideoCapture(0)

# this in input for the desired kernal sizes
KOPVAL = 3
KCLVAL = 10
#this defines the kenal used in noise reduction. the lower the kernal value the more precise but more noise
kernalOP=np.ones((KOPVAL,KOPVAL))
kernalCL=np.ones((KCLVAL,KCLVAL))
#NOTE!
# this needs to be refined
lowerBoundGreen = np.array([33,80,40])
upperBoundGreen = np.array([102,255,255])

# this gives input for the desired size of the image given by width. it is user input to deterime track quality
desImgSzWd = 250

# this gets the height of the image as a float value
width = goPro.get(3) 
height = goPro.get(4)
sizeratio = (width * 1.0) /height
desImgSzHt = (int)(desImgSzWd/sizeratio)
# this creats a font for feedback on the img
font=cv2.FONT_HERSHEY_SIMPLEX

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x)
        print(y)
        



#this loop keeps the camera open
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
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
            cv2.putText(img,str(i+1),(x,y+h),font,1,(0,255,255),2)
       
        #this provides an exit key
        if cv2.waitKey(2) == ord('s'):
                cv2.destroyAllWindows()
                break
        # this creats a window with a string title and takes an image as a peramiter
        cv2.setMouseCallback('check',draw_circle)
        cv2.imshow("check",img)
        cv2.imshow("MaskwKernalCL",maskClose)
        cv2.waitKey(10)
goPro.release()
