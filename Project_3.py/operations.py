import numpy as np
import convertion as cv

def sum (m1, m2):
    sum_1 = np.array(m1)
    sum_2 = np.array(m2)
    solution = sum_1 + sum_2
    return print(f'The sum of {sum_1} and {sum_2} is: {solution}')

def subtraction (m1, m2):
    sub_1 = np.array(m1)
    sub_2 = np.array(m2)
    solution = sub_1 - sub_2
    return print(f'The subtration between {sub_1} and {sub_2} is: {solution}')

'''def multiply (m1, m2):
    return solution

def determinant (m1):
    return solution

def transpose (m1):
    return solution

def diagonal (m1):
    return solution

def inverse (m1):
    return solution
'''
