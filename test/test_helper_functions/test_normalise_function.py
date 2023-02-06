"""Unit tests for normalise function"""
from unittest import TestCase
from src import helper_functions

class TestNormaliseFunctions(TestCase):
    """Unit tests for normalise functions"""

    def test_normalise_with_number_in_range(self):
        """Test normalise function with number within valid range"""
        num = helper_functions.normalise(100)
        self.assertEqual(num, 100)

    def test_nomralise_with_number_below_range(self):
        """Test normalise function with number below valid range"""
        num = helper_functions.normalise(90)
        self.assertEqual(num, 116)

    def test_nomralise_with_number_above_range(self):
        """Test normalise function with number above valid range"""
        num = helper_functions.normalise(130)
        self.assertEqual(num, 104)