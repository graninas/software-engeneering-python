
import sys






class Coords:
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth


class Meteor:
    __mass = 0
    __size = 0
    __coords = Coords(0, 0)

    def __init__(self, m, s, c):
        self.__mass = m
        self.__size = s
        self.__coords = c

    def getMass(self):
        return self.__mass
        self.__coords = c

    def getCoords(self):
        return self.__coords


if __name__ == "__main__":
    print("Hello World!")

    m = Meteor(10, 11, Coords(111, 222))

    print(m.getMass())
    print(m.getCoords().altitude)
    print(m.getCoords().azimuth)
