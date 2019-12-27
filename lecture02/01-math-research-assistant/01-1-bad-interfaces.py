### Lecture 2. Inversion of Control
### 01-1. Bad Interfaces

### SRP violated
### Not consistent
### Redundant
### Not documented

import sys

class Natural():
    def __init__(self):
        pass

    """ A popular descripiton. """
    def get_description(self):
        return "Natural is an integer number between 0 and infinity."

    def get_sample(self):
        return 42;

    def get_wikipedia_link():
        return "https://en.wikipedia.org/wiki/Natural_number"




if __name__ == "__main__":
    print("Math Research Assistant")

    nat = Natural()

    print(nat.get_description())
    print(nat.get_sample())
