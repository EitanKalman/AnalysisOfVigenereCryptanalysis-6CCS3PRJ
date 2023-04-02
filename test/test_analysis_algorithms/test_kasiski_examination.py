"""Unit tests for Kasiski Examination Analysis"""
from unittest import TestCase
from src.analysis_algorithms import kasiski_examination

class TestKasiskiExamination(TestCase):
    """Unit tests for Kasiski Examination Analysis"""

    def setUp(self):
        self.string = "thisisastringthisisnotastring"

    def test_repeated_substring_distances_with_non_empty_string(self):
        """Test repeated_substring_distances function with non-empty string"""
        distances = kasiski_examination._repeated_substring_distance(self.string)
        self.assertEqual(len(distances), 9)
        self.assertIn(13, distances)
        self.assertIn(16, distances)

    def test_repeated_substring_distances_with_empty_string(self):
        """Test repeated_substring_distances function with empty string"""
        distances = kasiski_examination._repeated_substring_distance("")
        self.assertEqual(len(distances), 0)

    def test_get_factors_with_non_zero(self):
        """Test get_factors function with non-zero positive number"""
        factors = kasiski_examination._get_factors(10)
        self.assertEqual(len(factors), 2)
        self.assertIn(2, factors)
        self.assertIn(5, factors)

    def test_get_factors_with_zero(self):
        """Test get_factors function with zero"""
        factors = kasiski_examination._get_factors(0)
        self.assertEqual(len(factors), 0)

    def test_get_possible_key_length(self):
        """Test get_possible_key_length function with non empty list"""
        ls = [522, 910, 321, 318, 630, 965, 335, 630, 630, 630, 630, 630, 630, 630,
              630, 405, 910, 315, 238, 321, 462, 392, 154, 392, 476, 238, 322, 84, 154,
              392, 476, 238, 322, 84, 504, 294, 190, 668, 350, 60, 322, 70, 238, 168,
              30, 280, 504, 552, 168, 168, 168, 168, 168, 168, 742, 574, 168, 526, 358,
              168, 168, 266, 630, 630, 487, 434, 238, 546, 425, 425, 420, 347, 345,
              84, 56, 350, 55, 349, 294, 140, 169, 247, 14, 294, 98, 160, 123, 120]
        possible_key_lengths = kasiski_examination._get_possible_key_length(ls)
        self.assertIn(14, possible_key_lengths)

    def test_get_possible_key_length_with_empty_list(self):
        """Test get_possible_key_length function with non empty list"""
        with self.assertRaises(ValueError):
            kasiski_examination._get_possible_key_length([])
