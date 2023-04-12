#!/usr/bin/python3

'''
module name: '0-add_integer'
included function:
    'add_integer'
'''


def add_integer(a, b=98):
    '''
    returns addition of integers
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
