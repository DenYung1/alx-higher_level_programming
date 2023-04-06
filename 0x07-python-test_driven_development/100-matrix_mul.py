#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.
    :param m_a: A list of lists of integers or floats.
    :param m_b: A list of lists of integers or floats.
    :return: The product of m_a and m_b as a new matrix.
    """
    # Check that m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    # Check that m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Check that m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    # Check that m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check that m_a is not empty
    if not m_a or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    
    # Check that m_b is not empty
    if not m_b or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    
    # Check that all elements in m_a are integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    
    # Check that all elements in m_b are integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    
    # Check that m_a is a rectangle
    a_num_cols = len(m_a[0])
    if any(len(row) != a_num_cols for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    # Check that m_b is a rectangle
    b_num_cols = len(m_b[0])
    if any(len(row) != b_num_cols for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Check that m_a and m_b can be multiplied
    if a_num_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Compute the product of m_a and m_b
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(b_num_cols):
            val = 0
            for k in range(a_num_cols):
                val += m_a[i][k] * m_b[k][j]
            row.append(val)
        result.append(row)
    
    # Return the product as a new matrix
    return result
 
