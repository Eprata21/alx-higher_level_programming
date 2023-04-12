#!/usr/bin/python3

"""
add attributes
"""


def add_attribute(obj, name, value):
    '''
    Adds attribute if possible
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
