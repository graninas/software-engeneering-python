### Lecture 2. Inversion of Control
### 01-1. Bad Interfaces

### SRP violated
### Not consistent
### Redundant
### Not documented

import sys
import random

import requests

class Natural():
    def __init__(self):
        pass

    def get_name(self):
        return "Natural number"

    """ A popular descripiton. """
    def get_description(self):
        return "Natural is an integer number between 0 and infinity."

    ### Redundancy: get_sample, get_random_sample
    ### Strange method with strange result.
    def get_sample(self):
        return 42;

    def get_random_sample(self):
        return random.randrange(0, 100)

    ### Redundancy: get_wikipedia_link, get_wikipedia_page
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Natural_number"

    ### Invalid responsibility (the definition class should not interact with the internet)
    ### Duplicated code across classes
    def get_wikipedia_page(self):
        r = requests.get(self.get_wikipedia_link())
        return r.content

### ------------------------------------------------------------------------

class Prime():
    def __init__(self):
        pass

    def get_name(self):
        return "Prime number"

    """ A popular descripiton. """
    def get_description(self):
        return """A prime number (or a prime) is a natural number greater
than 1 that cannot be formed by multiplying two smaller natural numbers."""

    ### Redundancy: get_sample, get_random_sample
    ### Strange method with strange result.
    def get_sample(self):
        return 7;

    def get_random_sample(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return primes[random.randrange(0, 25)]

    ### Redundancy: get_wikipedia_link, get_wikipedia_page
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Prime_number"

    ### Invalid responsibility (the definition class should not interact with the internet)
    ### Duplicated code across classes
    def get_wikipedia_page(self):
        r = requests.get(self.get_wikipedia_link())
        return r.content



if __name__ == "__main__":
    print("Math Research Assistant")

    nat = Natural()
    print(nat.get_description())
    print(nat.get_sample())
    print(nat.get_random_sample())
    print(nat.get_wikipedia_link())
    # print(nat.get_wikipedia_page())

    prime = Prime()
    print(prime.get_description())
    print(prime.get_sample())
    print(prime.get_random_sample())
    print(prime.get_wikipedia_link())
    # print(nat.get_wikipedia_page())
