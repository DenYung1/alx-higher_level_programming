#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns the result as a new matrix.
    :param matrix: A list of lists of integers or floats.
    :param div: A number (integer or float) to divide the matrix elements by.
    :return: A new matrix with the elements divided by div and rounded to 2 decimal places.
    """
    # Check that matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check that each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check that div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num/div, 2) for num in row] for row in matrix]
    
    # Return the new matrix
    return new_matrix
 
