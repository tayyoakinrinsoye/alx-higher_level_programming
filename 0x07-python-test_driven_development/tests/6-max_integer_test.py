#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([...])"""

    def test_ordered_list(self):
        """Test an ordered list"""
        ordered = [1,3,5,7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        """Test an unordered list"""
        unordered = [2,5,8,3]
        self.assertEqual(max_integer(unordered), 8)
        
    def test_max_at_beginning(self):
        """Test for maximum number at the beginning"""
        max_at_beginning = [10,5,7,3,4]
        self.assertEqual(max_integer(max_at_beginning), 10)

    def test_empty_list(self):
        """Test if list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        ''' Test for one element'''
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        ''' Test for float items'''
        floats = [2,3, 4.5, 5.6, 8.8]
        self.assertEqual(max_integer(floats), 8.8)

    def test_floats_and_ints(self):
        ''' Test for float and integer elements'''
        floats_and_ints = [1,2,3,5.6,7.8,9.2,10]
        self.assertEqual(max_integer(floats_and_ints), 10)

    def test_strings(self):
        '''Test for strings'''
        strings = "Elements"
        self.assertEqual(max_integer(strings), "t")

    def test_list_of_strings(self):
        '''Test for list of strings'''
        string_list = ["my", "name", "is", "tayo"]
        self.assertEqual(max_integer(string_list), "tayo")

    def test_empty_string(self):
        '''Test empty string'''
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()

