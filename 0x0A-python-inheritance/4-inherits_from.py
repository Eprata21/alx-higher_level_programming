#!/bin/bash/python3
"""
inherited_from
"""


def inherits_from(obj, a_class):
    """
    function that returns an instance of a class that inherited
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
