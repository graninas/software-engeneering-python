
import sys
import random
from abc import *
from enum import Enum
from services.knowledge_base.notion import *
from services.knowledge_base.math_object import *
from services.knowledge_base.knowledge_base import *



class KnowledgeBase(IKnowledgeBase):
    def __init__(self, obj_dict):
        self.__obj_dict = obj_dict

    def find_obj(self, obj_name):
        if obj_name in self.__obj_dict:
            return self.__obj_dict[obj_name]
        return None



def make_objects_dict_impl(obj_list):
    obj_dict = dict()
    for obj in obj_list:
        obj_dict[obj.get_name()] = obj
    return obj_dict

def make_objects_dict():
    prime_gen = PrimeGenerator()
    natural_gen = NaturalNumberGenerator()
    number_gen = NaturalNumberGenerator()
    circle_area_gen = CircleAreaGenerator()
    circle_area_formula = CircleAreaFormula()

    return make_objects_dict_impl(
        [ GenericMathObject("Prime", "Prime number", prime_gen, ConstEvaluator(prime_gen))
        , GenericMathObject("Natural", "Natural number", natural_gen, ConstEvaluator(natural_gen))
        , GenericMathObject("Number", "Number notion", number_gen, ConstEvaluator(number_gen))
        , GenericMathObject("circle_area", "Pi * R * R", circle_area_gen, circle_area_formula)
        ])

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

class PrimeGenerator(IGenerator):
    def __init__(self):
        self.__current = 0

    def max_generation(self):
        return 10

    def get_current(self):
        return primes[self.__current]

    def generate_next(self):
        if (self.__current + 1 >= self.max_generation()):
            raise Exception("Prime generator supports only first " + str(self.max_generation()) + " primes.")
        self.__current += 1
        return self.get_current()


class NaturalNumberGenerator(IGenerator):
    def __init__(self):
        self.__current = 0

    def max_generation(self):
        return -1

    def get_current(self):
        return self.__current

    def generate_next(self):
        self.__current += 1
        return self.get_current()

class ConstEvaluator(IEvaluable):
    def __init__(self, generator : IGenerator):
        self.__generator = generator

    def args_count(self):
        return 0

    def get_arg(self, arg_idx, arg: IEvaluable):
        raise Exception("Constant evaluator doesn't have any args.")

    def set_arg(self, arg_idx, arg: IEvaluable):
        raise Exception("Constant evaluator doesn't take any args.")

    def evaluate(self, args):
        return self.__generator.get_current()

class CircleAreaFormula(IEvaluable):
    def __init__(self):
        self.__radius = None

    def args_count(self):
        return 1

    def set_arg(self, arg_idx, arg):
        if (arg_idx != 0):
            raise Exception("Circle area formula takes only 1 arg.")

        self.__radius = arg

    def get_arg(self, arg_idx):
        if (arg_idx != 0):
            raise Exception("Circle area formula has only 1 arg.")

        return self.__radius

    def evaluate(self):
        if (self.__radius == None):
            raise Exception("Circle area argument (radius) is not set.")

        radius = self.__radius
        return radius *  radius * 3.1415


class CircleAreaGenerator(IGenerator):
    def __init__(self):
        circle_area_formula = CircleAreaFormula()
        circle_area_formula.set_arg(0, 1)

        self.__current_radius = 1
        self.__current_formula = circle_area_formula

    def max_generation(self):
        return -1

    def get_current(self):
        return self.__current_formula

    def generate_next(self):
        self.__current_radius += 1

        circle_area_formula = CircleAreaFormula()
        circle_area_formula.set_arg(0, self.__current_radius)

        self.__current_formula = circle_area_formula

        return self.get_current()
