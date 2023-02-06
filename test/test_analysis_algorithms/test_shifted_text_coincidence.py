"""Unit tests for Shifted Text Coincidence"""
from unittest import TestCase
from src.analysis_algorithms import shifted_text_coincidence

class TestShiftedTextCoincidence(TestCase):
    """Unit tests for Shifted Text Coincidence"""

    def test_add_padding_with_non_empty_string_and_positive_padding(self):
        """Test add_left_padding function with non empty string and positive padding"""
        padded = shifted_text_coincidence._add_left_padding("hello", 1)
        self.assertEqual(padded, " hello")

    def test_add_padding_with_non_empty_string_and_negative_padding(self):
        """Test add_left_padding function with non empty string and negative padding"""
        with self.assertRaises(ValueError):
            shifted_text_coincidence._add_left_padding("hello", -1)

    def test_add_padding_with_empty_string_and_positive_padding(self):
        """Test add_left_padding function with empty string and positive padding"""
        padded = shifted_text_coincidence._add_left_padding("", 1)
        self.assertEqual(padded, " ")

    def test_compare_same_length(self):
        """Test compare function with 2 texts of the same length"""
        coincidences = shifted_text_coincidence._compare("hello", "world")
        self.assertEqual(coincidences, 1)

    def test_compare_first_longer(self):
        """Test compare function with 2 texts where the first is longer than the second"""
        coincidences = shifted_text_coincidence._compare("hellow", "world")
        self.assertEqual(coincidences, 1)

    def test_compare_second_longer(self):
        """Test compare function with 2 texts where the second is longer than the first"""
        coincidences = shifted_text_coincidence._compare("hello", "worldd")
        self.assertEqual(coincidences, 1)