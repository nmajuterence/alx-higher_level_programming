#!/usr/bin/python3
# tests/max_integer_test.py

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
    
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
    
    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
    
    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")
    
    def test_mixed_data_types(self):
        self.assertEqual(max_integer(["apple", 2, 3.5]), "apple")

if __name__ == '__main__':
    unittest.main()
