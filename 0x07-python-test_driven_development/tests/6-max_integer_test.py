#!/usr/bin/python3
""" Unittest for the function max_integer """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maxint(self):
        """ Check each list, numbers, combinations"""
        self.assertEqual(max_integer([2, 2, 5]), 8)
        self.assertEqual(max_integer([10, 10, 10]), 10)
        self.assertEqual(max_integer([-41, -2, -1, 0, -95]), 0)
        self.assertEqual(max_integer([2.8, 7.1, 8.8]), 4.7)
        self.assertEqual(max_integer([76]), 76)

    def test_emptylist(self):
        """Test void list"""
        self.assertEqual(max_integer([]), None)

    def test_typeserror(self):
        """Test errors values raised when neccesary"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, (3 + 5j))
