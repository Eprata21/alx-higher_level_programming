#/bin/bash/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """sub class of base geametry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """defineing the area again"""
        return self.__width * self.__height
    def __str__(self):
        """method that returns the string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
