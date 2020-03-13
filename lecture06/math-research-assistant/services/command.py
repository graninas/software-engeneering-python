import sys
import random
from abc import *
from enum import Enum

from services.knowledge_base.knowledge_base import IKnowledgeBase

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def get_args_count(self): pass

    # Returns: (finish?, state, msg)
    @abstractmethod
    def evaluate(self, state, args, base : IKnowledgeBase): pass
