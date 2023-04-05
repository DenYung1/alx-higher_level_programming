#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    :param a: An integer or float.
    :param b: An integer or float.
    :return: The addition of a and b, casted to an integer.
    """
    # Check that a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    
    # Check that b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    # Return the sum of a and b, casted to an integer
    return int(a + b)
 
