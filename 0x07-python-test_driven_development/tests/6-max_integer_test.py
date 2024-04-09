#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_values(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, -3, -5, -2]), -2)

if __name__ == '__main__':
    unittest.main()
