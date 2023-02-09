"""Unit tests for run_analysis.py"""
from unittest import TestCase
from src import run_analysis

class TestRunAnalysis(TestCase):
    """Unit tests for run_analysis.py"""

    def test_generate_keys(self):
        """Test generate_keys function"""
        keys = run_analysis._generate_keys()
        self.assertEqual(len(keys), 10)
        for key in keys:
            self.assertNotEqual(len(key), 0)

    def test_generate_ciphertexts_with_valid_plaintexts_and_keys(self):
        """Test generate_ciphertexts function with valid plaintexts and valid keys"""
        plaintexts = ["helloworld", "teststring"]
        keys = ["dautac", "ayptm", "ajsptna"]
        ciphertexts = run_analysis._generate_ciphertexts(plaintexts, keys)
        self.assertEqual(len(ciphertexts), 2)
        self.assertEqual(len(ciphertexts[0]), 3)
        self.assertEqual(len(ciphertexts[1]), 3)

    def test_generate_ciphertexts_with_empty_plaintexts_and_valid_keys(self):
        """Test generate_ciphertexts function with empty plaintexts and valid keys"""
        plaintexts = []
        keys = ["dautac", "ayptm", "ajsptna"]
        with self.assertRaises(ValueError):
            run_analysis._generate_ciphertexts(plaintexts, keys)

    def test_generate_ciphertexts_with_non_empty_plaintexts_and_empty_keys(self):
        """Test generate_ciphertexts function with non_empty plaintexts and empty keys"""
        plaintexts = ["helloworld", "teststring"]
        keys = []
        with self.assertRaises(ValueError):
            run_analysis._generate_ciphertexts(plaintexts, keys)
        
    def test_generate_ciphertexts_with_empty_string_plaintext_and_valid_keys(self):
        """test generate_ciphertexts function with empty string plaintext and valid keys"""
        plaintexts = [""]
        keys = ["haplt"]
        ciphertexts = run_analysis._generate_ciphertexts(plaintexts, keys)
        self.assertEqual(len(ciphertexts), 1)
        self.assertEqual(len(ciphertexts[0]), 1)
        self.assertEqual(ciphertexts[0][0], "")

    def test_generate_ciphertexts_with_valid_plaintext_and_empty_keys(self):
        """test generate_ciphertexts function with empty string plaintext and valid keys"""
        plaintexts = ["helloworld", "teststring"]
        keys = [""]
        with self.assertRaises(AssertionError):
            run_analysis._generate_ciphertexts(plaintexts, keys)
