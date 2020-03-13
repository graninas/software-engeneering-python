import sys
import random
from abc import *
from enum import Enum

import requests
from math_object import MathObject
from resource_tag import ResourceTag

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
