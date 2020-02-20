import sys
import random
from abc import *
from enum import Enum

from services.command import IUserCommand
from services.knowledge_base.knowledge_base import IKnowledgeBase

class Finish(IUserCommand):
    def get_command_tag(self):
        return "finish"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args, base : IKnowledgeBase):
        return (True, state, "Finished.")

class Describe(IUserCommand):
    def get_command_tag(self):
        return "describe"

    def get_args_count(self):
        return 1

    def evaluate(self, state, args, base : IKnowledgeBase):
        if len(args) != 1:
            raise Exception("Invalid number of arguments.")

        found = base.find_obj(args[0])
        if found != None:
            return (False, state, found.get_description())
            
        return (False, state, "Object not found in DB: " + args[0])

class DescribeShort(Describe):
    def get_command_tag(self):
        return "d"
