
import sys
import random
from abc import *
from enum import Enum
from services.knowledge_base.notion import *
from services.knowledge_base.math_object import *
from services.knowledge_base.knowledge_base import *



class KnowledgeBase(IKnowledgeBase):
    def __init__(self, obj_dict):
        self.__obj_dict = obj_dict

    def find_obj(self, obj_name):
        if obj_name in self.__obj_dict:
            return self.__obj_dict[obj_name]
        return None



def make_objects_dict_impl(obj_list):
    obj_dict = dict()
    for obj in obj_list:
        obj_dict[obj.get_name()] = obj
    return obj_dict

def make_objects_dict():
    return make_objects_dict_impl(
        [ GenericMathObject("Prime", "Prime number")
        , GenericMathObject("Natural", "Natural number")
        , GenericMathObject("Number", "Number notion")
        ])
