import math

class Planet:
    def __init__(self, planet):
        self.moons = []
        self.planet = planet
class Pair:
    def __init__(self, planet, moon):
        self.planet = planet
        self.moon = moon
class Count:
    def __init__(self):
        self.counter = 0

def loadInput():
    f = open("daySix.txt", "r")
    planets = []
    for x in f:
        y = x.split(')')
        planets.append(Pair(y[0].strip('\n'), y[1].strip('\n')))
    return planets

def AddMoons(listOfPlanets, planet, count):
    for planetInList in listOfPlanets:
        if planetInList.planet == planet.planet:
            newPlanet = Planet(planetInList.moon)
            planet.moons.append(newPlanet)
            listOfPlanets.remove(planetInList)
            count.counter = count.counter + 1
            print("added planet ", count.counter)
            AddMoons(listOfPlanets, newPlanet, count)

planets = loadInput()
head = Planet(planets[0].planet)
head.moons.append(Planet(planets[0].moon))
planets.remove(planets[0])
AddMoons(planets, head, Count())

asd = "asd"




