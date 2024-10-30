#!/usr/bin/python3
""" access and update the private attributes"""
class Square:
   """ define class square attributes"""
    def size(self, value):

    """ showing attributes of square class """
        if type(size) is not int:

            raise TypeError ("size must be an integer")
        else:

            if size > 0:

               raise ValueError ("size must be >= 0")

        else:
            self.__size = value

    def __init__(self, size=0):

    """ initializing size of square"""
        self.size = size

    def area(self):
    """ return area of calculated square"""
        return (self.__size) ** 2
