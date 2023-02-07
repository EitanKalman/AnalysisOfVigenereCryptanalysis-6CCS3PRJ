"""Unit tests for key calculation"""
from collections import Counter
from unittest import TestCase
from src import calculate_key

class TestCalculateKey(TestCase):
    """Unit tests for key calculation"""

    def setUp(self):
        self.string = "thisisasamplestring"

    def test_chi_squared_with_non_empty_text(self):
        """Test chi_squared function with a non empty string"""
        frequencies = Counter(self.string)
        length = len(self.string)
        chi_squared = calculate_key._chi_squared(frequencies, length)
        self.assertEqual(chi_squared, 11.24673800417695)

    def test_shift_left_with_non_empty_text_with_positive_shift(self):
        """Test shift_left function with non empty string with a positive shift"""
        shifted_text = calculate_key._shift_left(self.string, 2)
        self.assertEqual(shifted_text, "rfgqgqyqyknjcqrpgle")

    def test_shift_left_with_non_empty_text_with_zero_shift(self):
        """Test shift_left function with non empty string with a shift of zero"""
        shifted_text = calculate_key._shift_left(self.string, 0)
        self.assertEqual(shifted_text, self.string)

    def test_shift_left_with_non_empty_text_with_negative_shift(self):
        """Test shift_left function with non empty string with a negative shift"""
        with self.assertRaises(ValueError):
            calculate_key._shift_left(self.string, -2)
