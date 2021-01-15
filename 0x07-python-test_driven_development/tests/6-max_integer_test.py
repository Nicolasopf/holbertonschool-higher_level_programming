#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        def test_maxint(self):
            """Test different number lists"""
            self.assertEqual(max_integer([15, 9, 6]), 15)
            self.assertEqual(max_integer([10, 10, 10]), 10)
            self.assertEqual(max_integer([-54, -7, 0, -84, -25]), 0)
            self.assertEqual(max_integer([4.8, 3.2, 9.2]), 9.2)
            self.assertEqual(max_integer([38]), 38)

        def test_emptylist(self):
            """Test void list"""
            self.assertEqual(max_integer([]), None)

        def test_typeserror(self):
            """Test errors values raised when neccesary"""
            self.assertRaises(TypeError, max_integer, None)
            self.assertRaises(TypeError, max_integer, (3 + 5j))
