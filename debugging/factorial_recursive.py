#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer.

    Parameters:
    - n (int): The integer for which the factorial is to be calculated.

    Returns:
    - int: The factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Getting input from command line argument and calculating factorial
f = factorial(int(sys.argv[1]))
print(f)
