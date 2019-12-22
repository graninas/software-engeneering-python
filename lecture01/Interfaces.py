### Interfaces in Python

import sys

### Option 1: Duck Typing

### Coords interface:
###
###   Returns a list of components in form (componentName, componentValue)
###   getComponents(self)


### Option 2: OOP interface
class ICoords:
    def getComponents(self):
        raise NotImplementedError('ICoords::getComponents() not implemented')

## Option 3: Abstract base class with ABCMeta & abstractmethod() approach
# import abc
# from abc import ABCMeta
#
# class CoordsBase(metaclass = ABCMeta):
#     @abstractmethod
#     def getComponents(self):
#         raise NotImplementedError('getComponents() not implemented')

## ------------------------------------------------------------------------- ##
# Option 1: Duck-typed interface implemented
class SphericalCoords:
    def __init__(self, dst, polar, azmth):
        self.distance = dst
        self.polarAngle = polar
        self.azimuthAngle = azmth

    # Duck-typed interface implemented.
    def getComponents(self):
        return [ ('distance', self.distance)
               , ('polarAngle', self.polarAngle)
               , ('azimuthAngle', self.azimuthAngle)
               ]

# Option 2: OOP interface implemented
class HorizontalCoords(ICoords):
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth

    def getComponents(self):
        return [('altitude', self.altitude), ('azimuth', self.azimuth)]

# Option 2: OOP interface not implemented
class HorizontalCoordsBroken(ICoords):
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth

    ### getComponents() from ICoords is not implemented!
    ### def getComponents(self):
    ###     return [('altitude', self.altitude), (azimuth, self.azimuth)]


class Meteor:
    __mass = 0
    __size = 0
    __coords = ICoords()

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
    print("Interfaces in Python.")

    m1 = Meteor(10, 11, HorizontalCoords(111, 222))
    print(m1.getMass())
    print(m1.getCoords().altitude)
    print(m1.getCoords().azimuth)
    print(m1.getCoords().getComponents())

    try:
        m2 = Meteor(10, 11, HorizontalCoordsBroken(111, 222))
        print(m2.getCoords().getComponents())
    except Exception:
        print("Exception got on accessing components.")

    m3 = Meteor(10, 11, SphericalCoords(10, 12, 33))
    print(m3.getCoords().getComponents())

    print("Printing coords using dynamic polymorphism.")

    coordsList = [ HorizontalCoords(111, 222)   # Using ICoords
                 , SphericalCoords(10, 12, 33)  # Using Duck Typing
                 , HorizontalCoords(555, 777)   # Using ICoords
                 ]

    for coord in coordsList:
        print(coord.getComponents())
