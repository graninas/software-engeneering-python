import sys
import random
from abc import *
from enum import Enum

from services.command import *
from services.knowledge_base.math_object import *
from services.knowledge_base.knowledge_base import *
from services.knowledge_base.notion import *
from impl.commands import *
from impl.knowledge_base import *


def parse_user_input(user_input):
    tokens = user_input.strip().split(" ")

    if len(tokens) == 0:
        return (None, None, "")

    norm_cmd = tokens[0].lower()

    if norm_cmd in supported_commands:
        cmd = supported_commands[norm_cmd]
        return (cmd, tokens[1:10], "")

    return (None, None, "Command not supported: ")

def eval_command(cmd : IUserCommand, args, st, base : IKnowledgeBase):
    if cmd.get_args_count() != len(args):
        return (False, st, "Invalid number of args. Expected: "
            + str(cmd.get_args_count()) + ", " + "got: " + str(len(args)))
    return cmd.evaluate(st, args, base)


def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ Finish()
    , Describe()
    , DescribeShort()
    ])


if __name__ == "__main__":
    print("Math Research Assistant")

    # prime_gen = PrimeGenerator()
    # natural_gen = NaturalNumberGenerator()
    # number_gen = NaturalNumberGenerator()
    # circle_area_gen = CircleAreaGenerator()

    # print(circle_area_gen.get_current())
    # print(circle_area_gen.generate_next())

    # formula = circle_area_gen.get_current()
    # print(formula.get_arg(0))
    # print(formula.evaluate())


    base = KnowledgeBase(make_objects_dict())

    finished = False
    state = ""
    message = ""
    args = []
    cmd = None
    try:
        while not(finished):
            user_input = input("$> ")

            cmd, args, message = parse_user_input(user_input)
            if cmd == None:
                print(message)
                continue
            (finished, state, message) = eval_command(cmd, args, state, base)
            print("New state: " + str(state))
            if message != "": print(message)
    except:
        print("Unexpected error:", sys.exc_info()[0])
