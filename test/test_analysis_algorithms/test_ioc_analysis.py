"""Unit tests for Index of Coincidence Analysis"""
from unittest import TestCase
from src.analysis_algorithms import ioc_analysis
from src import helper_functions

class TestIOCAnalysis(TestCase):
    """Unit tests for Index of Coincidence Analysis"""

    def setUp(self):
        self.string = "thisisasamplestring"

    def test_calculate_text_ioc_for_lowercase_non_empty_text(self):
        """Test calculate_text_ioc with a lowercase text"""
        ioc = ioc_analysis._calculate_text_ioc(self.string)
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_empty_text(self):
        """Test calculate_text_ioc with an empty text"""
        ioc = ioc_analysis._calculate_text_ioc("")
        self.assertEqual(ioc, 0)

    def test_calculate_text_ioc_for_uppercase_non_empty_text(self):
        """Test calculate_text_ioc with an uppercase text"""
        ioc = ioc_analysis._calculate_text_ioc(self.string.upper())
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_text_ioc_for_mixed_non_empty_text(self):
        """Test calculate_text_ioc with a text with mixed upper and lowercase"""
        ioc = ioc_analysis._calculate_text_ioc("ThisIsASampleString")
        self.assertEqual(ioc, 0.06432748538011696)

    def test_calculate_ioc_average_for_non_empty_text(self):
        """Test calculate_ioc_average for a lowercase text"""
        split_ciphertext = helper_functions.split(self.string, 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_empty_text(self):
        """Test calculate_ioc_average for an empty text"""
        split_ciphertext = helper_functions.split("", 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0)

    def test_calculate_ioc_average_for_uppercase_non_empty_text(self):
        """Test calculate_ioc_average for an uppercase text"""
        split_ciphertext = helper_functions.split(self.string.upper(), 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)

    def test_calculate_ioc_average_for_mixed_non_empty_text(self):
        """Test calculate_ioc_average for a text with mixed upper and lowercase"""
        split_ciphertext = helper_functions.split("ThisIsASampleString", 2)
        average_ioc = ioc_analysis._calculate_ioc_average(split_ciphertext)
        self.assertEqual(average_ioc, 0.1388888888888889)
