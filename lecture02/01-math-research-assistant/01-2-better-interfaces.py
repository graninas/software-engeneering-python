### Lecture 2. Inversion of Control
### 01-2. Better Interfaces

import sys
import random
from abc import *

import requests

class MathObject(metaclass = ABCMeta):

    @abstractmethod
    def get_name(self): pass

    @abstractmethod
    def get_description(self): pass

    ### Invalid responsibility (why it knows about Wikipedia?)
    ### Invalid design: what about other langauges, other resources?
    @abstractmethod
    def get_wikipedia_link(): pass

### ------------------------------------------------------------------------

class NumberBase(MathObject, metaclass = ABCMeta):

    @abstractmethod
    def get_random_sample(): pass

### ------------------------------------------------------------------------

class Number(NumberBase):

    def get_name(self):
        return "Number"

    def get_description(self):
        return "A number is a mathematical object used to count, measure, and label."

    def get_random_sample(self):
        return random.randrange(0, 100)

    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Number"

### ------------------------------------------------------------------------

class Natural(NumberBase):

    def get_name(self):
        return "Natural number"

    def get_description(self):
        return "Natural is an integer number between 0 and infinity."

    def get_random_sample(self):
        return random.randrange(0, 100)

    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Natural_number"

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

    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Prime_number"

### ------------------------------------------------------------------------

class WikipediaDownloader():

    def __init__(self, math_object : MathObject):
        self.__link = math_object.get_wikipedia_link()

    def download_content(self):
        r = requests.get(self.__link)
        return r.content

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
    print(nat.get_wikipedia_link())

    prime = Prime()
    print(prime.get_name())
    print(prime.get_description())
    print(prime.get_random_sample())
    print(prime.get_wikipedia_link())

    num = Number()
    print(num.get_name())
    print(num.get_description())
    print(num.get_random_sample())
    print(num.get_wikipedia_link())

    wiki_downloader = WikipediaDownloader(prime)
    print(wiki_downloader.download_content())
