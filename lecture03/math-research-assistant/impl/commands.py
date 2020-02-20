import sys
import random
from abc import *
from enum import Enum

from services.command import IUserCommand

class Finish(IUserCommand):
    def get_command_tag(self):
        return "finish"

    def get_args_count(self):
        return 0

    def evaluate(self, state):
        return (True, state, "Finished.")

class Describe(IUserCommand):
    def get_command_tag(self):
        return "describe"

    def get_args_count(self):
        return 1

    def evaluate(self, state):
        return (False, state, "")
