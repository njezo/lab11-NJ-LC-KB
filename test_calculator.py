# https://github.com/njezo/lab11-NJ-LC-KB/tree/615473fc20e58d2186e0028c1c3ce93342e62975/Lab%20Repository
# Partner 1: Your Name
# Partner 2: Lydia Zhao

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -2), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 20), 4)
        self.assertEqual(divide(1, 7), 7)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(25), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
