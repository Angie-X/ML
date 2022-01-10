import math
import turtle
from Planet import *
from Moon import *
from SolarSystem import *
from Sun import *


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
    # As you can see from the orange line leading offscreen to the right,
    # even these parameters eventually slingshotted this poor moon!
    #
    # don't forget to add the moon to this planet before the planet is added
    # to the Solar System!
    ss.addPlanet(m)

    m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
    # add moons here for testing?
    moon1 = Moon("Virus", 5, 800, .2, 0, 50, "indigo", m)
    moon2 = Moon("Germs",8, 300, .1, 0, 80, "pink", m)
    m.addMoon(moon1)
    m.addMoon(moon2)
    ss.addPlanet(m)

    m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
    # add moons here for testing?
    m1 = Moon("LittleM", 5, 200, .1, 0, 105, "orange", m)
    m.addMoon(m1)
    ss.addPlanet(m)

    m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
    # add moons here for testing?
    m1 = Moon("Convid-19",10,2000,0.2,0,150,"black",m)
    m.addMoon(m1)
    ss.addPlanet(m)

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()




createSSandAnimate()
