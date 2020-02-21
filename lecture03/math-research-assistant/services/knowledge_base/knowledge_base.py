import sys
import random
from abc import *
from enum import Enum
from services.knowledge_base.math_object import IMathObject


class IKnowledgeBase(metaclass = ABCMeta):

    @abstractmethod
    def find_obj(self, obj_name : str) -> IMathObject:
        pass
