### Lecture 2. Inversion of Control
### 01-3. Math Knowledge Base

import sys
import random
from abc import *
from enum import Enum

import math_object
import resource_downloader

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

class Finish(IUserCommand):
    def get_command_tag(self):
        return "finish"

def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ Finish()

    ])

def is_finish_command(cmd):
    return cmd.get_command_tag() == Finish().get_command_tag()

def is_invalid_command(cmd):
    return cmd == None

def normalize_command(user_input):
    return user_input.strip().lower()

def parse_user_input(user_input):
    norm_cmd = normalize_command(user_input)
    if norm_cmd in supported_commands:
        return supported_commands[norm_cmd]
    return None

def eval_command(cmd):
    pass

if __name__ == "__main__":
    print("Math Research Assistant")

    do_loop = True
    while do_loop:
        user_input = input("$> ")
        mb_cmd = parse_user_input(user_input)
        if is_invalid_command(mb_cmd):
            print("Invalid command.")
        elif is_finish_command(mb_cmd):
            do_loop = False
        else:
            eval_command(mb_cmd)
