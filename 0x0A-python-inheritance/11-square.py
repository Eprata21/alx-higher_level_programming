#/bin/bash/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class of rectangle
"""
class Square(Rectangle):
    """ class square"""
    def __init__(self, size):
        """ function that define the area"""

        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """method that define area again"""
        return self.__size ** 2
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
