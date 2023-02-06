"""Unit tests for vigenere function"""
from unittest import TestCase
from src.helper_functions import vigenere

class TestVigenereFunction(TestCase):
    """Unit tests for vigenere function"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"
        self.string_with_spaces = "this is a sample string"
        self.key = "crypto"
        self.ciphertext = "vyghbgcjybizgjrgbbi"
        self.ciphertext_with_spaces = "vygh bg c jybizg jrgbbi"

    def test_vigenere_encrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.string_without_spaces, self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.string_without_spaces.upper(), self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.string_without_spaces, self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.string_without_spaces.upper(), self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_decrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.ciphertext, self.key, False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a lowercase key, both without spaces"""
        ciphertext = vigenere(self.ciphertext.upper(), self.key, False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a uppercase key, both without spaces"""
        ciphertext = vigenere(self.ciphertext, self.key.upper(), False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a uppercase key, both without spaces"""
        ciphertext = vigenere(self.ciphertext.upper(), self.key.upper(), False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_encrypt_with_lowercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext with spaces and a lowercase key"""
        ciphertext = vigenere(self.string_with_spaces, self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext with spaces and a uppercase key"""
        ciphertext = vigenere(self.string_with_spaces.upper(), self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext with spaces and a uppercase key"""
        ciphertext = vigenere(self.string_with_spaces, self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext with spaces and a uppercase key"""
        ciphertext = vigenere(self.string_with_spaces.upper(), self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_decrypt_with_lowercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext with spaces and a lowercase key"""
        plaintext = vigenere(self.ciphertext_with_spaces, self.key, False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a lowercase key"""
        plaintext = vigenere(self.ciphertext_with_spaces.upper(), self.key, False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_lowercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext with spaces and a uppercase key"""
        plaintext = vigenere(self.ciphertext_with_spaces, self.key.upper(), False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext with spaces and a uppercase key"""
        plaintext = vigenere(self.ciphertext_with_spaces.upper(), self.key.upper(), False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_encrypt_with_lowercase_text_and_lowercase_key_with_spaces(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, with spaces"""
        ciphertext = vigenere(self.string_without_spaces, "cry pto", True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_and_uppercase_key_with_spaces(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key with spaces"""
        ciphertext = vigenere(self.string_without_spaces, "cry pto", True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_text_with_non_letters(self):
        """Test vigenere function with a text that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            vigenere("textcontaining1", "crypto", True)

    def test_vigenere_encrypt_with_key_with_non_letters(self):
        """Test vigenere function with a key that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            vigenere(self.string_without_spaces, "crypto1", True)