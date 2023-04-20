#!/usr/bin/python3
"""
class rectangle from module basre
"""

from models.base import Base


class Rectangle(Base):
    """ class rectang """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initalization a rectangle class instance """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width attributes """

        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width attributes """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value <= 0:
            ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height attributes """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """  getter for x attributes """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for y attributes """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """ public method tha returns the area of rectangle """

        return self.height * self.width

    def display(self):
        """ print the stdout of the instance """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' self.__width)

    def __str__(self):

        """ returning the string representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
