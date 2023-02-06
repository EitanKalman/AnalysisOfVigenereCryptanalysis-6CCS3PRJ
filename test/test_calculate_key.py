"""Unit tests for key calculation"""
from unittest import TestCase
from src import calculate_key
from src import helper_functions

class TestCalculateKey(TestCase):
    """Unit tests for key calculation"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"

    def test_chi_squared_with_non_empty_text(self):
        """Test chi_squared function with a non empty string without spaces"""
        frequencies = helper_functions.frequency_analysis(self.string_without_spaces)
        length = len(self.string_without_spaces)
        chi_squared = calculate_key._chi_squared(frequencies, length)
        self.assertEqual(chi_squared, 11.24673800417695)

    def test_shift_left_with_non_empty_text_with_positive_shift(self):
        """Test shift_left function with non empty string without spaces with a positive shift"""
        shifted_text = calculate_key._shift_left(self.string_without_spaces, 2)
        self.assertEqual(shifted_text, "rfgqgqyqyknjcqrpgle")

    def test_shift_left_with_non_empty_text_with_zero_shift(self):
        """Test shift_left function with non empty string without spaces with a shift of zero"""
        shifted_text = calculate_key._shift_left(self.string_without_spaces, 0)
        self.assertEqual(shifted_text, self.string_without_spaces)

    def test_shift_left_with_non_empty_text_with_negative_shift(self):
        """Test shift_left function with non empty string without spaces with a negative shift"""
        with self.assertRaises(ValueError):
            calculate_key._shift_left(self.string_without_spaces, -2)
