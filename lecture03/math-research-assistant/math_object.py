import sys
import random
from abc import *
from enum import Enum

import requests

"""Represents an abstract math concept."""
class MathObject(metaclass = ABCMeta):

    """Returns a name."""
    @abstractmethod
    def get_name(self): pass

    """Returns a short description."""
    @abstractmethod
    def get_description(self): pass

    """Returns a dictionary of resources:
    dict<ResourceTag, ResourceUrl>
    """
    @abstractmethod
    def get_resources(): pass
