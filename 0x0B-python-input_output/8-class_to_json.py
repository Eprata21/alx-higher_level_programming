#!/usr/bin/python3

"""
class to json
"""


def class_to_json(obj):
    """ function that returns the dictionary
    description
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
