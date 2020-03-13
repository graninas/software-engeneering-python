import sys
import random
from abc import *
from enum import Enum
from services.knowledge_base.notion import INotion

class IGenerator(metaclass = ABCMeta):
    @abstractmethod
    def max_generation(self):
        pass

    @abstractmethod
    def get_current(self):
        pass

    @abstractmethod
    def generate_next(self):
        pass

class IEvaluable(metaclass = ABCMeta):
    @abstractmethod
    def args_count(self):
        pass

    @abstractmethod
    def get_arg(self, arg_idx):
        pass

    @abstractmethod
    def set_arg(self, arg_idx, arg):
        pass

    @abstractmethod
    def evaluate(self, args):
        pass

class IMathObject(INotion, metaclass = ABCMeta):

    @abstractmethod
    def get_generator(self) -> IGenerator:
        pass

    @abstractmethod
    def get_evaluable(self) -> IEvaluable:
        pass

class GenericMathObject(IMathObject):
    def __init__(self, name : str, description : str, generator: IGenerator, evaluable: IEvaluable):
        self.__name = name
        self.__description = description
        self.__generator = generator
        self.__evaluable = evaluable

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_generator(self) -> IGenerator:
        return self.__generator

    def get_evaluable(self) -> IEvaluable:
        return self.__evaluable
