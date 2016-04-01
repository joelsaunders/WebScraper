import doctest
import unittest
import utils

class Test(unittest.TestCase):
    """ Unit tests for utils"""
    def test_doctests(self):
        doctest.testmod(utils)
        

if __name__ == "__main__":
    unittest.main()
