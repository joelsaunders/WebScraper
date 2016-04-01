import doctest
import unittest
import scraperprogram

class Test(unittest.TestCase):
    """ Unit tests for scraperprogram"""
    def test_doctests(self):
        doctest.testmod(scraperprogram)
        

if __name__ == "__main__":
    unittest.main()
