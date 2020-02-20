import sys
import random
from abc import *
from enum import Enum

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def get_args_count(self): pass

    @abstractmethod
    def evaluate(self, state): pass     # Returns: (finish?, state, msg)
