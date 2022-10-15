#!/usr/bin/python3
'''Function that prints square'''

def print_square(size):
    """print a square

        Args:
            Size(int): size of the square to be printed

        Raises:
            TypeError: if size is non integer
            ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
