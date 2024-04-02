#!/usr/bin/python3
"""Class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__"""
        self.size = size
        self.position = position

    def area(self):
        """area"""
        return self.__size**2

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(isinstance(i, int) is not True for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """my_print"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
