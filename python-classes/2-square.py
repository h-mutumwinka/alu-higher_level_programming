#!/usr/bin/python3
""" Define a class called square"""
 

 class Square:
 """Define a class square"""

    def __init__(self,size=0):
        """initialize size of the square class """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size > 0
            raise ValueError(size must be >= 0)
        else:
            self.__size = size
