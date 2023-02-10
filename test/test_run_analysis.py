"""Unit tests for run_analysis.py"""
from unittest import TestCase
from src import run_analysis

class TestRunAnalysis(TestCase):
    """Unit tests for run_analysis.py"""

    def setUp(self):
        self.plaintext = "thisisasamplestring"
        self.key = "crypto"
        self.ciphertext = "vyghbgcjybizgjrgbbi"
        self.ciphertext_with_spaces = "vygh bg c jybizg jrgbbi"

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

    def test_vigenere_encrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.plaintext, self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.plaintext.upper(), self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.plaintext, self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.plaintext.upper(), self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_decrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.ciphertext, self.key, False)
        self.assertEqual(ciphertext, self.plaintext)

    def test_vigenere_decrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a lowercase key"""
        ciphertext = run_analysis._vigenere(self.ciphertext.upper(), self.key, False)
        self.assertEqual(ciphertext, self.plaintext)

    def test_vigenere_decrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a uppercase key"""
        ciphertext = run_analysis._vigenere(self.ciphertext, self.key.upper(), False)
        self.assertEqual(ciphertext, self.plaintext)

    def test_vigenere_decrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a uppercase key"""
        ciphertext = run_analysis._vigenere(self.ciphertext.upper(), self.key.upper(), False)
        self.assertEqual(ciphertext, self.plaintext)

    def test_vigenere_encrypt_with_text_with_non_letters(self):
        """Test vigenere function with a text that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            run_analysis._vigenere("textcontaining1", "crypto", True)

    def test_vigenere_encrypt_with_key_with_non_letters(self):
        """Test vigenere function with a key that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            run_analysis._vigenere(self.plaintext, "crypto1", True)
