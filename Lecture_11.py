# 11. Problems in Software Engineering
# ------------------------------------

- Requirements can be (mostly are) badly defined.
- Decisions are full of compromises (goals, requirements, simplicity)
- Tight deadlines


# OOP problems

- Multiple inheritance (anti-pattern)
- Buidling taxonomies
- Inheritance
- Long chain of inheritance (Violation of Demetra's law)
- Ellipse-circle problem (Square-rectangle problem)
    # https://en.wikipedia.org/wiki/Circle%E2%80%93ellipse_problem
- Diamond problem (Violation of Liskov Substitution Principle) (SOLID: https://twitter.com/unclebobmartin/status/1253752012728131585)
- Public Morozov


class Vehicle:
    startEngine():
        klflfldlsf

class HasWeel:
    pass

class Car(Vehicle, HasWeel):
    startEngine()

class Airplane(Vehicle, HasWeel):
    startEngine()

class WaterAirPlane(Airplane):
    startEngine(self):
        super()

# Vehicle -> Airplane -> WaterAirPlane

1. Interfaces
1a. Small, single base class
2. Composition (OOP composition)

class Weels:
    pass

class Enigne:
    start():
        pass

class Vehicle:
    def __init__(self, weels, engine):
        self._weels = weels
        self._engine = engine
        self._weels_count = weels.count()

    def startEngine(self):
        if (self._engine is not None):
            self._engine.start()


class Car:
    def __init__(self):
        self._vehicle = Vehicle(Weels(), Engine())

class Car(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(Weels(), Engine())

class Airplane(Vehicle):
    def __init__(self, waterSlidingPlanks):
        ...

# Ellipse-circle problem

# Ellipse 2 axis
# Circle is an ellipse with 2 equal axis


class Ellipse:
    def __init__(self, x, y):
        self._x = x
        self._y = y

#    def stretchX(self, dx):
#        self._x = self._x + dx

#    def stretchY(self, dy):
#        self._x = self._x + dx

    def stretch(self, dx, dy):
        self._x = self._x + dx
        self._x = self._x + dx


class Circle(Ellipse):
    def __init__(self, d):
        super(Ellipse, self).__init__(d, d)

    def stretch(self, dx, dy):
        if (dx != dy):
            raise Exception('Invalid argument')


circle = Circle(10)

circle.stretchX(11000)

# Diamond problem

# abstract base class
class Vehicle:
    @abstractmethod
    def startEngine(): pass

class Car(Vehicle):
    def startEngine(self):
        #implement somehow
        print('Engines started (car)')

class Scooter(Vehicle):
    def startEngine(self):
        #implement somehow
        print('Engines started (scooter)')

class TukTuk(Car, Scooter):
    def startEngine(self):
        # ??? what startEngine to use?
        super(Car, self).startEngine()
        super(Scooter, self).startEngine()

# Long chain of inheritance

class A: pass
class B(A): pass
class C(B): pass
class D(C): pass

# Public Morozov

class Vehicle:
    def __init__(self, weels, engine):
        self.__weels = weels
        self.__engine = engine
        self.__usage_count = 0

    def startEngine(self):
        self.__usage_count += 1
        self.__engine.start()

    def service_needed(self):
        return self.__engine.resource() <= self.__usage_count

class Car(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(Weels(), Engine())

    def startEngine():              # Public Morozov
        self.__engine.start()
