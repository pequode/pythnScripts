''' this is the Point class
this class is in charge of holding an x and y value and
the methods for aproximating another point
it is a rough draft
@author George Kent-Scheller
@version 07162018 
'''
class Point:
    def __init__(self,xPos,yPos):
        self.x = xPos
        self.y = yPos
    def aproxT(self,lstPnt):
        # uses order to determine which point is being used first to determin sign 
        # then it finds the slope between the two points
        # and applys the sign transformation.
        # this is very much a placeholder for a better method
        
        # the addition of 1.0 is to stop the int data type from trunkating
        deltaY = 1.0*(self.y - lstPnt.y)
        deltaX = 1.0*(self.x - lstPnt.x)
        slope = (int)(deltaY/deltaX)
        # now the deltaX is added to the lstPnts X cordinate
       
        # this next section takes care of the vector component that i couldnt deal with 
        direc = 0
        if (self.x>lstPnt.x):
            direc = -1
        else:
            direc = 1
        newX = (direc * abs(deltaX)) + lstPnt.x
        # this is just algebra
        newY = slope*(newX -self.x) + self.y
      
        return Point(newX,newY)
    def getDistanceBetween (self,snd):
        return (abs(self.x-snd.x)**2 +abs(self.y-snd.y)**2)**0.5


