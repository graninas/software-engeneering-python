import sys
import random
from abc import *
from enum import Enum


class IKnowledgeBase(metaclass = ABCMeta):

    @abstractmethod
    def find_obj(self, obj_name): pass
