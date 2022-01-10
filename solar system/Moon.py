# class Moon:

# TODO: Add a Moon class! You should start by copying most of the code from Planets.
# Feel free to alter it to make the moons more distinct (perhaps
# pick a different shape for them?). Be sure to uncomment the class line above
# when you're ready to test this class.
#
# Make the following additional changes to this Moon class:
#
# -- an instance variable planet that indicates which Planet object the
#    moon belongs to. This should be passed in as an additional parameter
#    in the Moon constructor. Be sure to create the Planet before you create any
#    of its Moons, or you won't have an object to pass in for this parameter!
# -- in the Moon class, __distance represents the distance from the associated Planet,
#    not the Sun. To set a Moon's initial __x, add __distance to the __x value of
#    its Planet.
# -- include getters for the Moon's name and its Planet (the former is a string, the latte
#    is a Planet object).

import math
import turtle


class Moon:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC,iPlanet):
        self.__name = iName
        self.__planet = iPlanet
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy

        self.__x = self.__distance + self.__planet.getXPos()
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("turtle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy


    def __str__(self):
        return self.__name

    def getPlanet(self):
        return self.__planet