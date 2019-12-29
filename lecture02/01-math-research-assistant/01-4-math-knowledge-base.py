### Lecture 2. Inversion of Control
### 01-3. Math Knowledge Base

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

### ------------------------------------------------------------------------

class NumberBase(MathObject, metaclass = ABCMeta):

    @abstractmethod
    def get_random_sample(): pass

### ------------------------------------------------------------------------

class ResourceTag(Enum):
     WIKIPEDIA = 1

### ------------------------------------------------------------------------

class Number(NumberBase):

    def get_name(self):
        return "Number"

    def get_description(self):
        return "A number is a mathematical object used to count, measure, and label."

    def get_random_sample(self):
        return random.randrange(0, 100)

    def get_resources(self):
        return dict([(ResourceTag.WIKIPEDIA, "https://en.wikipedia.org/wiki/Number")])

### ------------------------------------------------------------------------

class Natural(NumberBase):

    def get_name(self):
        return "Natural number"

    def get_description(self):
        return "Natural is an integer number between 0 and infinity."

    def get_random_sample(self):
        return random.randrange(0, 100)

    def get_resources(self):
        return dict([(ResourceTag.WIKIPEDIA, "https://en.wikipedia.org/wiki/Natural_number")])

### ------------------------------------------------------------------------

class Prime(NumberBase):

    def get_name(self):
        return "Prime number"

    def get_description(self):
        return """A prime number (or a prime) is a natural number greater
than 1 that cannot be formed by multiplying two smaller natural numbers."""

    def get_random_sample(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return primes[random.randrange(0, 25)]

    def get_resources(self):
        return dict([(ResourceTag.WIKIPEDIA, "https://en.wikipedia.org/wiki/Prime_number")])

### ------------------------------------------------------------------------

### Uses MathObject as interface (IoC principle)
### No error processing.
### No validation.
### Method returns None on case of absent tag.
### Direct downloading (not async).
"""Resource downloader."""
class ResourceDownloader():

    def __init__(self, math_object : MathObject, resource_tag: ResourceTag):
        self.__math_object = math_object
        self.__resource_tag = resource_tag

    def download_content(self):
        resources = self.__math_object.get_resources()
        if self.__resource_tag in resources:
            url = resources[self.__resource_tag]
            r = requests.get(url)
            return r.content

        return None

### ------------------------------------------------------------------------




### ------------------------------------------------------------------------

if __name__ == "__main__":
    print("Math Research Assistant")

    ### Cannot be instantiated: abstract class.
    # mo = MathObject()
    # print(mo.get_name())
    # print(mo.get_description())

    ### Cannot be instantiated: abstract class.
    # nb = NumberBase()
    # print(nb.get_random_sample())

    nat = Natural()
    print(nat.get_name())
    print(nat.get_description())
    print(nat.get_random_sample())
    print(nat.get_resources())

    prime = Prime()
    print(prime.get_name())
    print(prime.get_description())
    print(prime.get_random_sample())
    print(prime.get_resources())

    num = Number()
    print(num.get_name())
    print(num.get_description())
    print(num.get_random_sample())
    print(num.get_resources())

    resource_downloader = ResourceDownloader(prime, ResourceTag.WIKIPEDIA)
    content = resource_downloader.download_content()
    if content:
        #print(content)
        print("Content found and downloaded.")
    else:
        print("No content found for WIKIPEDIA resource.")
