import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

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
          
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX/r**3
            accY = G * self.__theSun.getMass() * rY/r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

            # TODO: Uncomment the following line once you've written the moveMoons method.
            # It should move all the moons associated with Planet p before the for-loop
            # iterates to the next planet.
            p.moveMoons()

    def freeze(self):
        self.__ssScreen.exitonclick() 

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

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()

        self.__moons = []

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

    def showMoons(self):
        for aMoon in self.__moons:
            print(aMoon)

    def addMoon(self, aMoon):
        self.__moons.append(aMoon)

    def removeMoon(self, aMoon):
        for theMoon in self.__moons:
            if theMoon == aMoon:
                self.__moons.remove(theMoon)

    def moveMoons(self):
        G = .1
        dt = .001

        for aMoon in self.__Moons:
            aMoon.moveTo(aMoon.getXPos() + dt * aMoon.getXVel(),
                         aMoon.getYPos() + dt * aMoon.getYVel())

            rX = self.__getXPos() - aMoon.getXPos()
            rY = self.__getYPos() - aMoon.getYPos()

            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.__getMass() * rX / r ** 3
            accY = G * self.__getMass() * rY / r ** 3

            aMoon.setXVel(aMoon.getXVel() + dt * accX)
            aMoon.setYVel(aMoon.getYVel() + dt * accY)


    # TODO: add getters and setters for Moon objects in the moons instance variable here

    # def moveMoons():

        # TODO: Write this method as described above! Uncomment the def line above
        # once you're ready to test it.

class Moon:

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


    def __str__(self):
        return self.__name

    def getPlanet(self):
        return self.__planet

def createSSandAnimate():

    # This is a testing method for the entire module. Make
    # changes as you see fit to test the system out overall,
    # then add lines that add moons to planets before they
    # are stored in the SolarSystem when you're ready to test
    # the Moon and Planet code you've written.
    
   ss = SolarSystem(2, 2)

   sun = Sun("Sun", 5000, 10, 5800)
   ss.addSun(sun)

   m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
   # add moons here for testing?
   # your code should look something like this, with values instead of text:
   # moon1 = Moon("Moon 1", radius, mass, distance from planet,
   #              0, initial y-velocity, moon color, m)
   # since m is the Planet that was just created, a reference will be stored
   # to it in the Moon object before m is used to create a new planet
   #
   # Hint: orbital mechanics is HARD. You will need to play around
   # with the initial values (distance from planet, mass, and y-velocity)
   # for a while before you get a moon that actually orbits its planet
   # instead of slingshotting out of the solar system.
   #
   # Here are the values for a moon added to Mars that produced the
   # jpeg I added to the assignment:
   #
   # m1 = Moon("LittleM", 5, 200, .1, 0, 105, "orange", m)
   #
   # As you can see from the orange line leading offscreen to the right,
   # even these parameters eventually slingshotted this poor moon!
   #
   # don't forget to add the moon to this planet before the planet is added
   # to the Solar System!
   ss.addPlanet(m)

   m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
   moon1 = Moon("Virus", 5, 200, .1, 0, 105, "grey", m)
   moon2 = Moon("Germs", 8, 300, .2, 0, 105, "grey", m)
   m.addMoon(moon1)
   m.addMoon(moon2)
   # add moons here for testing?

   ss.addPlanet(m)

   m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
   # add moons here for testing?
   m1 = Moon("LittleM", 5, 200, .1, 0, 105, "orange", m)
   m.addMoon(m1)
   ss.addPlanet(m)

   m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
   # add moons here for testing?
   ss.addPlanet(m)

   numTimePeriods = 2000
   for aMove in range(numTimePeriods):
        ss.movePlanets()

   ss.freeze()

createSSandAnimate()