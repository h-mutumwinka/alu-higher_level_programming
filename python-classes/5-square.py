#!/usr/bin/python3
""" Define a class called Square"""
class Square:
    def size(self, value):
        """setting size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    def __init__(self, size=0):    
        """ showing size of squqre area"""
        self.size = size

    def size (self):
        """retriving size of square"""
        return self.__size

    def area(self):
        """calculates the square's area Returns:The area of the square"""
    
        return (self.__size) ** 2    
    def my_print(self):
        """prints the square returning nothing"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
