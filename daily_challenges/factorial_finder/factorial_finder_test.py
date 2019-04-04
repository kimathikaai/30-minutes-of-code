import unittest
from factorial_finder import factorial

class TestFactorialFinder(unittest.TestCase):
    def test_factorial_finder(self):
        expected = ( (0,1),(1,1),(2,2),(3,6),(9,362880) )
        for key, value in expected:
            self.assertEqual(value, factorial(key))

if __name__  == "__main__":
    unittest.main()
