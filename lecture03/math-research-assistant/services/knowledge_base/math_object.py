import sys
import random
from abc import *
from enum import Enum
from services.knowledge_base.notion import INotion

class IMathObject(INotion, metaclass = ABCMeta):

    @abstractmethod
    def get_description(self) -> str:
        pass



class GenericMathObject(IMathObject):
    def __init__(self, name : str, description : str):
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description
