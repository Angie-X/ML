import math
import turtle

class Sun:
   def __init__(self, iName, iRad, iM, iTemp):
       self.__name = iName
       self.__radius = iRad
       self.__mass = iM
       self.__temp = iTemp
       self.__x = 0
       self.__y = 0

       self.__sTurtle = turtle.Turtle()
       self.__sTurtle.shape("circle")
       self.__sTurtle.color("yellow")

   def getMass(self):
       return self.__mass

   def getXPos(self):
       return self.__x

   def getYPos(self):
       return self.__y
