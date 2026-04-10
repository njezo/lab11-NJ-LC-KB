# https://github.com/njezo/lab11-NJ-LC-KB/tree/615473fc20e58d2186e0028c1c3ce93342e62975/Lab%20Repository
# Partner 1: [Your Name]
# Partner 2: Lydia Zhao

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
def log (a, b):
    return math.log(a, b)
def exp(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
