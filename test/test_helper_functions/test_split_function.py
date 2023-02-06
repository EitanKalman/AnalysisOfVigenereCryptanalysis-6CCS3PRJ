"""Unit tests for split function"""
from unittest import TestCase
from src.helper_functions import split

class TestSplitFunctions(TestCase):
    """Unit tests for split function"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"
        # self.string_with_spaces = "this is a sample string"   -----------> need to add test cases for this

    def test_split_non_empty_string_with_non_zero_split(self):
        """Test split function with a non-empty string without spaces with a positive non-zero split"""
        split_text = split(self.string_without_spaces, 2)
        self.assertEqual(len(split_text), 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")

    def test_split_non_empty_string_with_one_split(self):
        """Test split function with a non-empty string without spaces with a split of one"""
        split_text = split(self.string_without_spaces, 1)
        self.assertEqual(len(split_text), 1)
        self.assertEqual(split_text[0], self.string_without_spaces)

    def test_split_non_empty_string_with_zero_split(self):
        """Test split function with a non-empty string without spaces with a split of zero"""
        with self.assertRaises(ValueError):
            split(self.string_without_spaces, 0)

    def test_split_non_empty_string_with_negative_split(self):
        """Test split function with a non-empty string without spaces with a negative split"""
        with self.assertRaises(ValueError):
            split(self.string_without_spaces, -2)

    def test_split_non_empty_string_with_positive_fraction_split(self):
        """Test split function with a non-empty string without spaces with a positive fractional split"""
        with self.assertRaises(TypeError):
            split(self.string_without_spaces, 2.5)

    def test_split_non_empty_string_with_negative_fraction_split(self):
        """Test split function with a non-empty string without spaces with a positive fractional split"""
        with self.assertRaises(ValueError):
            split(self.string_without_spaces, -2.5)

    def test_split_empty_string_with_non_zero_split(self):
        """Test split function with an empty string with a positive non-zero split"""
        split_text = split("", 2)
        self.assertEqual(len(split_text), 2)
        self.assertEqual(split_text[0], "")
        self.assertEqual(split_text[1], "")

    def test_split_empty_string_with_one_split(self):
        """Test split function with an empty string with a split of one"""
        split_text = split("", 1)
        self.assertEqual(len(split_text), 1)
        self.assertEqual(split_text, [""])

    def test_split_empty_string_with_zero_split(self):
        """Test split function with an empty string with a split of zero"""
        with self.assertRaises(ValueError):
            split("", 0)

    def test_empty_string_with_negative_split(self):
        """Test split function with an empty string with a negative split"""
        with self.assertRaises(ValueError):
            split("", -2)

    def test_empty_string_with_positive_fraction_split(self):
        """Test split function with an empty string with a positive fractional split"""
        with self.assertRaises(ValueError):
            split("", -2)

    def test_split_empty_string_with_negative_fraction_split(self):
        """Test split function with an empty string with a positive fractional split"""
        with self.assertRaises(ValueError):
            split("", -2.5)

    def test_split_with_uppercase_text(self):
        """Test split function with uppercase text"""
        split_text = split(self.string_without_spaces.upper(), 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")

    def test_split_with_mixed_case_text(self):
        """Test split function with text with mixed upper and lower case"""
        split_text = split("ThisIsASampleString", 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")