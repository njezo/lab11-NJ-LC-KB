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
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)
def exponent(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

# Aliases to satisfy Kaizen
sub = subtract
mul = multiply
div = divide
log = logarithm
exp = exponent
