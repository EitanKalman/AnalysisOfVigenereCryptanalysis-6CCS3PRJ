"""Unit tests for frequency analysis function"""
from unittest import TestCase
from src.helper_functions import frequency_analysis

class TestFrequencyAnalysisFunctions(TestCase):
    """Unit tests for frequency analysis functions"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"
        self.string_with_spaces = "this is a sample string" 

    def test_frequency_analysis_lowercase_string(self):
        """test frequency_analysis function with a lowercase string"""
        frequencies = frequency_analysis(self.string_without_spaces)
        self._assert_letter_frequencies(frequencies)

    def test_frequency_analysis_empty_string(self):
        """test frequency_analysis function with an empty string"""
        frequencies = frequency_analysis("")
        self.assertTrue(len(frequencies) == 0)

    def test_frequency_analysis_string_with_spaces(self):
        """test frequency_analysis function with a lowercase string with spaces"""
        frequencies = frequency_analysis(self.string_with_spaces)
        self._assert_letter_frequencies(frequencies)

    def test_frequency_analysis_uppercase_string(self):
        """test frequency_analysis function with a lowercase string"""
        frequencies = frequency_analysis(self.string_without_spaces.upper())
        self._assert_letter_frequencies(frequencies)

    def _assert_letter_frequencies(self, frequencies):
        self.assertFalse(len(frequencies) == 0)
        self.assertEqual(frequencies['a'], 2)
        self.assertEqual(frequencies['e'], 1)
        self.assertEqual(frequencies['g'], 1)
        self.assertEqual(frequencies['h'], 1)
        self.assertEqual(frequencies['i'], 3)
        self.assertEqual(frequencies['l'], 1)
        self.assertEqual(frequencies['m'], 1)
        self.assertEqual(frequencies['n'], 1)
        self.assertEqual(frequencies['p'], 1)
        self.assertEqual(frequencies['r'], 1)
        self.assertEqual(frequencies['s'], 4)
        self.assertEqual(frequencies['t'], 2)
