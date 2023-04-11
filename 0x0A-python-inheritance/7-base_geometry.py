#!/bin/bash/python3
"""
module with class basegeometry
"""


class BaseGeometry():
    """class basegeometry"""

    @classmethod
    def area(self):
        """funtion that calculate area"""
        raise Exception("area() is not implemented")

    @classmethod
    def integer_validator(self, name, value):
        """function tha validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
