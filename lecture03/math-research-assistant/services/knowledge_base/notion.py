import sys
import random
from abc import *
from enum import Enum

class INotion(metaclass = ABCMeta):

    @abstractmethod
    def get_name(self) -> str:
        pass
