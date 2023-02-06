"""Unit tests for Index of Coincidence Analysis"""
from unittest import TestCase
from src.analysis_algorithms import ioc_analysis
from src import helper_functions

class TestIOCAnalysis(TestCase):
    """Unit tests for Index of Coincidence Analysis"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"
        self.string_with_spaces = "this is a sample string"

    def test_calculate_text_ioc_for_lowercase_non_empty_text_without_spaces(self):
        """Test calculate_text_ioc with a lowercase text without spaces"""
        ioc = ioc_analysis._calculate_text_ioc(self.string_without_spaces)
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_lowercase_non_empty_text_with_spaces(self):
        """Test calculate_text_ioc with a lowercase text with spaces"""
        ioc = ioc_analysis._calculate_text_ioc(self.string_with_spaces)
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_empty_text(self):
        """Test calculate_text_ioc with an empty text"""
        ioc = ioc_analysis._calculate_text_ioc("")
        self.assertEqual(ioc, 0)

    def test_calculate_text_ioc_for_uppercase_non_empty_text_without_spaces(self):
        """Test calculate_text_ioc with an uppercase text without spaces"""
        ioc = ioc_analysis._calculate_text_ioc(self.string_without_spaces.upper())
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_uppercase_non_empty_text_with_spaces(self):
        """Test calculate_text_ioc with an uppercase text with spaces"""
        ioc = ioc_analysis._calculate_text_ioc(self.string_with_spaces.upper())
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_mixed_non_empty_text_without_spaces(self):
        """Test calculate_text_ioc with a text without spaces with mixed upper and lowercase"""
        ioc = ioc_analysis._calculate_text_ioc("ThisIsASampleString")
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_mixed_non_empty_text_with_spaces(self):
        """Test calculate_text_ioc with a text with spaces with mixed upper and lowercase"""
        ioc = ioc_analysis._calculate_text_ioc("This Is A Sample String")
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_ioc_average_for_non_empty_text_without_spaces(self):
        """Test calculate_ioc_average for a lowercase text without spaces"""
        split_ciphertext = helper_functions.split(self.string_without_spaces, 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_non_empty_text_with_spaces(self):
        """Test calculate_ioc_average for a lowercase text with spaces"""
        split_ciphertext = helper_functions.split(self.string_with_spaces, 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_empty_text(self):
        """Test calculate_ioc_average for an empty text"""
        split_ciphertext = helper_functions.split("", 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0)

    def test_calculate_ioc_average_for_uppercase_non_empty_text_without_spaces(self):
        """Test calculate_ioc_average for an uppercase text without spaces"""
        split_ciphertext = helper_functions.split(self.string_without_spaces.upper(), 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_uppercase_non_empty_text_with_spaces(self):
        """Test calculate_ioc_average for an uppercase text with spaces"""
        split_ciphertext = helper_functions.split(self.string_with_spaces.upper(), 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_mixed_non_empty_text_without_spaces(self):
        """Test calculate_ioc_average for a text without spaces with mixed upper and lowercase"""
        split_ciphertext = helper_functions.split("ThisIsASampleString", 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_mixedcase_non_empty_text_with_spaces(self):
        """Test calculate_ioc_average for a text with spaces with mixed upper and lowercase"""
        split_ciphertext = helper_functions.split("This Is A Sample String", 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)
