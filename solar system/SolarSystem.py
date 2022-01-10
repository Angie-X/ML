import turtle
import math
from Planet import *
from Moon import *


class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width / 2.0, -height / 2.0,
                                            width / 2.0, height / 2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()

            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.__theSun.getMass() * rX / r ** 3
            accY = G * self.__theSun.getMass() * rY / r ** 3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

            # TODO: Uncomment the following line once you've written the moveMoons method.
            # It should move all the moons associated with Planet p before the for-loop
            # iterates to the next planet.
            p.moveMoons()

    def freeze(self):
        self.__ssScreen.exitonclick()
