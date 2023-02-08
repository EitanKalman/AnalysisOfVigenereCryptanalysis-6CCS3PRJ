"""Unit tests for shift_char function"""
from unittest import TestCase
from src.helper_functions import shift_char

class TestShiftCharFunctions(TestCase):
    """Unit tests for shift_char functions"""

    def test_shift_char_lowercase_char_with_positive_shift(self):
        """Test shift_char function with a lowercase character with positive shift"""
        new_char = shift_char('g', 1)
        self.assertEqual(new_char, 'h')

    def test_shift_char_lowercase_lower_boundary_char_with_positive_shift(self):
        """Test shift_char function with a lower boundary lowercase character with positive shift"""
        new_char = shift_char('a', 1)
        self.assertEqual(new_char, 'b')

    def test_shift_char_lowercase_upper_boundary_char_with_positive_shift(self):
        """Test shift_char function with an upper boundary lowercase character with positive shift"""
        new_char = shift_char('z', 1)
        self.assertEqual(new_char, 'a')

    def test_shift_char_lowercase_char_with_negative_shift(self):
        """Test shift_char function function with a lowercase character with negative shift"""
        new_char = shift_char('g', -1)
        self.assertEqual(new_char, 'f')

    def test_shift_char_lowercase_lower_boundary_char_with_negative_shift(self):
        """Test shift_char function with a lower boundary lowercase character with negative shift"""
        new_char = shift_char('a', -1)
        self.assertEqual(new_char, 'z')

    def test_shift_char_lowercase_upper_boundary_char_with_negative_shift(self):
        """Test shift_char function with an upper boundary lowercase character with negative shift"""
        new_char = shift_char('z', -1)
        self.assertEqual(new_char, 'y')

    def test_shift_char_lowercase_char_with_large_positive_shift(self):
        """Test shift_char function with a lowercase character with large positive shift"""
        new_char = shift_char('g', 100)
        self.assertEqual(new_char, 'c')

    def test_shift_char_lowercase_char_with_large_negative_shift(self):
        """Test shift_char function with a lowercase character with a large negative shift"""
        new_char = shift_char('t', -100)
        self.assertEqual(new_char, 'x')

    def test_shift_char_lowercase_char_with_fractional_positive_shift(self):
        """Test shift_char function with a lowercase character with a fractional positive shift"""
        with self.assertRaises(TypeError):
            shift_char('t', 2.5)

    def test_shift_char_lowercase_char_with_fractional_negative_shift(self):
        """Test shift_char function with a lowercase character with a fractional negative shift"""
        with self.assertRaises(TypeError):
            shift_char('t', -2.5)

    def test_shift_char_uppercase_char_with_positive_shift(self):
        """Test shift_char function with a uppercase character with a positive shift"""
        new_char = shift_char('G', 1)
        self.assertEqual(new_char, 'h')

    def test_shift_char_uppercase_lower_boundary_char_with_positive_shift(self):
        """Test shift_char function with a lower boundary uppercase character with a positive shift"""
        new_char = shift_char('A', 1)
        self.assertEqual(new_char, 'b')

    def test_shift_char_uppercase_upper_boundary_char_with_positive_shift(self):
        """Test shift_char function with an upper boundary uppercase character with a positive shift"""
        new_char = shift_char('Z', 1)
        self.assertEqual(new_char, 'a')

    def test_shift_char_uppercase_char_with_negative_shift(self):
        """Test shift_char function function with a uppercase character with a negative shift"""
        new_char = shift_char('G', -1)
        self.assertEqual(new_char, 'f')

    def test_shift_char_uppercase_lower_boundary_char_with_negative_shift(self):
        """Test shift_char function with a lower-bound uppercase character with a negative shift"""
        new_char = shift_char('A', -1)
        self.assertEqual(new_char, 'z')

    def test_shift_char_uppercase_upper_boundary_char_with_negative_shift(self):
        """Test shift_char function with a upper-bound uppercase character with a negative shift"""
        new_char = shift_char('Z', -1)
        self.assertEqual(new_char, 'y')

    def test_shift_char_uppercase_char_with_large_positive_shift(self):
        """Test shift_char function with a uppercase character with a large positive shift"""
        new_char = shift_char('G', 100)
        self.assertEqual(new_char, 'c')

    def test_shift_char_uppercase_char_with_large_negative_shift(self):
        """Test shift_char function with a uppercase character with a large negative shift"""
        new_char = shift_char('T', -100)
        self.assertEqual(new_char, 'x')

    def test_shift_char_uppercase_char_with_fractional_positive_shift(self):
        """Test shift_char function with a uppercase character with a fractional positive shift"""
        with self.assertRaises(TypeError):
            shift_char('T', 2.5)

    def test_shift_char_uppercase_char_with_fractional_negative_shift(self):
        """Test shift_char function with a uppercase character with a fractional negative shift"""
        with self.assertRaises(TypeError):
            shift_char('T', -2.5)

    def test_shift_char_space(self):
        """Test shift_char_function with a space character"""
        with self.assertRaises(AssertionError):
            shift_char(' ', 2)

    def test_shift_char_non_letter(self):
        """Test shift_char_function with a non letter character"""
        with self.assertRaises(AssertionError):
            shift_char('#', 2)

    def test_shift_char_string(self):
        """Test shift_char function with a string"""
        with self.assertRaises(TypeError):
            shift_char('tf', 2)
