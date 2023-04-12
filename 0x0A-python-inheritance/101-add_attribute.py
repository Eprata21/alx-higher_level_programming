#!/usr/bin/python3

"""
functionn that adds new  attributes
"""


def add_attribte(obj, name, value):
    """ function that add attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
