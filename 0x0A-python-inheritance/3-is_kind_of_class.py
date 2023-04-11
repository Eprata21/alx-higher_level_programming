#/bin/bash/python3
"""
class is kind of class
"""
def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
