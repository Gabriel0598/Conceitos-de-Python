import unittest

class TestAbsFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(abs(10), 10)
        
    def test_negative_number(self):
        self.assertEqual(abs(-10), 10)
        
    def test_zero(self):
        self.assertEqual(abs(0), 0)