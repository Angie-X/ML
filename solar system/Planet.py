import math
import turtle
from Moon import *

class Planet:

    # TODO: Add the following to the Planet class:
    #
    # -- an instance variable called moons (a list of Moon objects belonging to that Planet)
    # -- an accessor method ("getter") that returns the instance variable moons
    # -- a getter that returns a list of the moon names
    # -- mutator methods ("setters") for adding and removing Moon objects from moons
    #    NOTE: for the remove setter, you should pass in a moon name as a parameter,
    #    then search through the moons list by comparing the target name to the name
    #    of each moon, then finally removing the matching Moon object. You should use
    #    the remove function of lists and an iterable for-loop to accomplish this.
    #    The syntax for the remove function is: list.remove(thingToBeRemoved)
    # -- a moveMoons method, similar to the movePlanets method of the SolarSystem class,
    #    that goes through moons and updates the position and velocities of each moon
    #    belonging to that Planet. You can start by copying code from the movePlanets
    #    method of the SolarSystem class, but be sure to alter it so that every Moon's
    #    position is updated relative to its associated Planet, not the Sun!

    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy

        # -- an instance variable called moons (a list of Moon objects belonging to that Planet)
        self.__moons = []

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def getMass(self):
        return self.__mass

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy

    # TODO: add getters and setters for Moon objects in the moons instance variable here

    # -- an accessor method ("getter") that returns the instance variable moons
    # -- a getter that returns a list of the moon names

    def showMoons(self):
        for aMoon in self.__moons:
            print(aMoon)

    # -- mutator methods ("setters") for adding and removing Moon objects from moons
    #    NOTE: for the remove setter, you should pass in a moon name as a parameter,
    #    then search through the moons list by comparing the target name to the name
    #    of each moon, then finally removing the matching Moon object. You should use
    #    the remove function of lists and an iterable for-loop to accomplish this.
    #    The syntax for the remove function is: list.remove(thingToBeRemoved)
    def addMoon(self, aMoon):
        self.__moons.append(aMoon)

    def removeMoon(self, aMoon):
        for theMoon in self.__moons:
            if theMoon == aMoon:
                self.__moons.remove(theMoon)



    # def moveMoons():
    def moveMoons(self):
        G = .1
        dt = .001

        for aMoon in self.__moons:
            aMoon.moveTo(aMoon.getXPos() + dt * aMoon.getXVel(),
                     aMoon.getYPos() + dt * aMoon.getYVel())

            rX = self.getXPos() - aMoon.getXPos()
            rY = self.getYPos() - aMoon.getYPos()

            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.getMass() * rX / r ** 3
            accY = G * self.getMass() * rY / r ** 3

            aMoon.setXVel(aMoon.getXVel() + dt * accX)
            aMoon.setYVel(aMoon.getYVel() + dt * accY)

    # TODO: Write this method as described above! Uncomment the def line above
    # once you're ready to test it.
