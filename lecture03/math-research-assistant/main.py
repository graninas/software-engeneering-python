### Lecture 2. Inversion of Control
### 01-3. Math Knowledge Base

import sys
import random
from abc import *
from enum import Enum

import math_object
import resource_downloader
from services.command import *
from impl.commands import *

def parse_user_input(user_input):
    norm_cmd = normalize_command(user_input)
    if norm_cmd in supported_commands:
        return supported_commands[norm_cmd]
    return None

def eval_command(cmd : IUserCommand, st):
    def is_invalid_command(cmd : IUserCommand):
        return cmd == None

    if is_invalid_command(mb_cmd):
        return (True, st, "Invalid command.")

    return cmd.evaluate(st)

def normalize_command(user_input):
    return user_input.strip().lower()

def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ Finish()
    , Describe()
    ])


if __name__ == "__main__":
    print("Math Research Assistant")

    finished = False
    state = ""
    message = ""
    try:
        while not(finished):
            user_input = input("$> ")
            mb_cmd = parse_user_input(user_input)
            finished, state, message = eval_command(mb_cmd, state)
            print("New state: " + str(state))
            if message != "": print(message)
    except:
        print("Unexpected error:", sys.exc_info()[0])
