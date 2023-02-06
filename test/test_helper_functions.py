"""Unit tests for helper functions"""
from unittest import TestCase
from src import helper_functions

class TestHelperFunctions(TestCase):
    """Unit tests for helper functions"""

    def setUp(self):
        self.string_without_spaces = "thisisasamplestring"
        self.string_with_spaces = "this is a sample string"
        self.key = "crypto"
        self.ciphertext = "vyghbgcjybizgjrgbbi"
        self.ciphertext_with_spaces = "vygh bg c jybizg jrgbbi"

    def test_vigenere_encrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces, self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces.upper(), self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces, self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces.upper(), self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_decrypt_with_lowercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.ciphertext, self.key, False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_and_lowercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a lowercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.ciphertext.upper(), self.key, False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_lowercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext and a uppercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.ciphertext, self.key.upper(), False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_and_uppercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a uppercase key, both without spaces"""
        ciphertext = helper_functions.vigenere(self.ciphertext.upper(), self.key.upper(), False)
        self.assertEqual(ciphertext, self.string_without_spaces)

    def test_vigenere_encrypt_with_lowercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext with spaces and a lowercase key"""
        ciphertext = helper_functions.vigenere(self.string_with_spaces, self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext with spaces and a uppercase key"""
        ciphertext = helper_functions.vigenere(self.string_with_spaces.upper(), self.key, True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function encryption with a lowercase plaintext with spaces and a uppercase key"""
        ciphertext = helper_functions.vigenere(self.string_with_spaces, self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_uppercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function encryption with a uppercase plaintext with spaces and a uppercase key"""
        ciphertext = helper_functions.vigenere(self.string_with_spaces.upper(), self.key.upper(), True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_decrypt_with_lowercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext with spaces and a lowercase key"""
        plaintext = helper_functions.vigenere(self.ciphertext_with_spaces, self.key, False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_with_spaces_and_lowercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext and a lowercase key"""
        plaintext = helper_functions.vigenere(self.ciphertext_with_spaces.upper(), self.key, False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_lowercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function decryption with a lowercase ciphertext with spaces and a uppercase key"""
        plaintext = helper_functions.vigenere(self.ciphertext_with_spaces, self.key.upper(), False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_decrypt_with_uppercase_text_with_spaces_and_uppercase_key(self):
        """Test vigenere function decryption with a uppercase ciphertext with spaces and a uppercase key"""
        plaintext = helper_functions.vigenere(self.ciphertext_with_spaces.upper(), self.key.upper(), False)
        self.assertEqual(plaintext, self.string_without_spaces)

    def test_vigenere_encrypt_with_lowercase_text_and_lowercase_key_with_spaces(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key, with spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces, "cry pto", True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_lowercase_text_and_uppercase_key_with_spaces(self):
        """Test vigenere function encryption with a lowercase plaintext and a lowercase key with spaces"""
        ciphertext = helper_functions.vigenere(self.string_without_spaces, "cry pto", True)
        self.assertEqual(ciphertext, self.ciphertext)

    def test_vigenere_encrypt_with_text_with_non_letters(self):
        """Test vigenere function with a text that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            helper_functions.vigenere("textcontaining1", "crypto", True)

    def test_vigenere_encrypt_with_key_with_non_letters(self):
        """Test vigenere function with a key that contains characters that aren't letters"""
        with self.assertRaises(AssertionError):
            helper_functions.vigenere(self.string_without_spaces, "crypto1", True)

    def test_split_non_empty_string_with_non_zero_split(self):
        """Test split function with a non-empty string without spaces with a positive non-zero split"""
        split_text = helper_functions.split(self.string_without_spaces, 2)
        self.assertEqual(len(split_text), 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")

    def test_split_non_empty_string_with_one_split(self):
        """Test split function with a non-empty string without spaces with a split of one"""
        split_text = helper_functions.split(self.string_without_spaces, 1)
        self.assertEqual(len(split_text), 1)
        self.assertEqual(split_text[0], self.string_without_spaces)

    def test_split_non_empty_string_with_zero_split(self):
        """Test split function with a non-empty string without spaces with a split of zero"""
        with self.assertRaises(ValueError):
            helper_functions.split(self.string_without_spaces, 0)

    def test_split_non_empty_string_with_negative_split(self):
        """Test split function with a non-empty string without spaces with a negative split"""
        with self.assertRaises(ValueError):
            helper_functions.split(self.string_without_spaces, -2)

    def test_split_non_empty_string_with_positive_fraction_split(self):
        """Test split function with a non-empty string without spaces with a positive fractional split"""
        with self.assertRaises(TypeError):
            helper_functions.split(self.string_without_spaces, 2.5)

    def test_split_non_empty_string_with_negative_fraction_split(self):
        """Test split function with a non-empty string without spaces with a positive fractional split"""
        with self.assertRaises(ValueError):
            helper_functions.split(self.string_without_spaces, -2.5)

    def test_split_empty_string_with_non_zero_split(self):
        """Test split function with an empty string with a positive non-zero split"""
        split_text = helper_functions.split("", 2)
        self.assertEqual(len(split_text), 2)
        self.assertEqual(split_text[0], "")
        self.assertEqual(split_text[1], "")

    def test_split_empty_string_with_one_split(self):
        """Test split function with an empty string with a split of one"""
        split_text = helper_functions.split("", 1)
        self.assertEqual(len(split_text), 1)
        self.assertEqual(split_text, [""])

    def test_split_empty_string_with_zero_split(self):
        """Test split function with an empty string with a split of zero"""
        with self.assertRaises(ValueError):
            helper_functions.split("", 0)

    def test_empty_string_with_negative_split(self):
        """Test split function with an empty string with a negative split"""
        with self.assertRaises(ValueError):
            helper_functions.split("", -2)

    def test_empty_string_with_positive_fraction_split(self):
        """Test split function with an empty string with a positive fractional split"""
        with self.assertRaises(ValueError):
            helper_functions.split("", -2)

    def test_split_empty_string_with_negative_fraction_split(self):
        """Test split function with an empty string with a positive fractional split"""
        with self.assertRaises(ValueError):
            helper_functions.split("", -2.5)

    def test_split_with_uppercase_text(self):
        """Test split function with uppercase text"""
        split_text = helper_functions.split(self.string_without_spaces.upper(), 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")

    def test_split_with_mixed_case_text(self):
        """Test split function with text with mixed upper and lower case"""
        split_text = helper_functions.split("ThisIsASampleString", 2)
        self.assertEqual(split_text[0], "tiiaapetig")
        self.assertEqual(split_text[1], "hsssmlsrn")

    def test_shift_char_lowercase_char_with_positive_shift(self):
        """Test shift_char function with a lowercase character with positive shift"""
        new_char = helper_functions.shift_char('g', 1)
        self.assertEqual(new_char, 'h')

    def test_shift_char_lowercase_lower_boundary_char_with_positive_shift(self):
        """Test shift_char function with a lower boundary lowercase character with positive shift"""
        new_char = helper_functions.shift_char('a', 1)
        self.assertEqual(new_char, 'b')

    def test_shift_char_lowercase_upper_boundary_char_with_positive_shift(self):
        """Test shift_char function with an upper boundary lowercase character with positive shift"""
        new_char = helper_functions.shift_char('z', 1)
        self.assertEqual(new_char, 'a')

    def test_shift_char_lowercase_char_with_negative_shift(self):
        """Test shift_char function function with a lowercase character with negative shift"""
        new_char = helper_functions.shift_char('g', -1)
        self.assertEqual(new_char, 'f')

    def test_shift_char_lowercase_lower_boundary_char_with_negative_shift(self):
        """Test shift_char function with a lower boundary lowercase character with negative shift"""
        new_char = helper_functions.shift_char('a', -1)
        self.assertEqual(new_char, 'z')

    def test_shift_char_lowercase_upper_boundary_char_with_negative_shift(self):
        """Test shift_char function with an upper boundary lowercase character with negative shift"""
        new_char = helper_functions.shift_char('z', -1)
        self.assertEqual(new_char, 'y')

    def test_shift_char_lowercase_char_with_large_positive_shift(self):
        """Test shift_char function with a lowercase character with large positive shift"""
        new_char = helper_functions.shift_char('g', 100)
        self.assertEqual(new_char, 'c')

    def test_shift_char_lowercase_char_with_large_negative_shift(self):
        """Test shift_char function with a lowercase character with a large negative shift"""
        new_char = helper_functions.shift_char('t', -100)
        self.assertEqual(new_char, 'x')

    def test_shift_char_lowercase_char_with_fractional_positive_shift(self):
        """Test shift_char function with a lowercase character with a fractional positive shift"""
        with self.assertRaises(TypeError):
            helper_functions.shift_char('t', 2.5)

    def test_shift_char_lowercase_char_with_fractional_negative_shift(self):
        """Test shift_char function with a lowercase character with a fractional negative shift"""
        with self.assertRaises(TypeError):
            helper_functions.shift_char('t', -2.5)

    def test_shift_char_uppercase_char_with_positive_shift(self):
        """Test shift_char function with a uppercase character with a positive shift"""
        new_char = helper_functions.shift_char('G', 1)
        self.assertEqual(new_char, 'h')

    def test_shift_char_uppercase_lower_boundary_char_with_positive_shift(self):
        """Test shift_char function with a lower boundary uppercase character with a positive shift"""
        new_char = helper_functions.shift_char('A', 1)
        self.assertEqual(new_char, 'b')

    def test_shift_char_uppercase_upper_boundary_char_with_positive_shift(self):
        """Test shift_char function with an upper boundary uppercase character with a positive shift"""
        new_char = helper_functions.shift_char('Z', 1)
        self.assertEqual(new_char, 'a')

    def test_shift_char_uppercase_char_with_negative_shift(self):
        """Test shift_char function function with a uppercase character with a negative shift"""
        new_char = helper_functions.shift_char('G', -1)
        self.assertEqual(new_char, 'f')

    def test_shift_char_uppercase_lower_boundary_char_with_negative_shift(self):
        """Test shift_char function with a lower boundary uppercase character with a negative shift"""
        new_char = helper_functions.shift_char('A', -1)
        self.assertEqual(new_char, 'z')

    def test_shift_char_uppercase_upper_boundary_char_with_negative_shift(self):
        """Test shift_char function with an upper boundary uppercase character with a negative shift"""
        new_char = helper_functions.shift_char('Z', -1)
        self.assertEqual(new_char, 'y')

    def test_shift_char_uppercase_char_with_large_positive_shift(self):
        """Test shift_char function with a uppercase character with a large positive shift"""
        new_char = helper_functions.shift_char('G', 100)
        self.assertEqual(new_char, 'c')

    def test_shift_char_uppercase_char_with_large_negative_shift(self):
        """Test shift_char function with a uppercase character with a large negative shift"""
        new_char = helper_functions.shift_char('T', -100)
        self.assertEqual(new_char, 'x')

    def test_shift_char_uppercase_char_with_fractional_positive_shift(self):
        """Test shift_char function with a uppercase character with a fractional positive shift"""
        with self.assertRaises(TypeError):
            helper_functions.shift_char('T', 2.5)

    def test_shift_char_uppercase_char_with_fractional_negative_shift(self):
        """Test shift_char function with a uppercase character with a fractional negative shift"""
        with self.assertRaises(TypeError):
            helper_functions.shift_char('T', -2.5)

    def test_shift_char_space(self):
        """Test shift_char_function with a space character"""
        with self.assertRaises(AssertionError):
            helper_functions.shift_char(' ', 2)

    def test_shift_char_non_letter(self):
        """Test shift_char_function with a non letter character"""
        with self.assertRaises(AssertionError):
            helper_functions.shift_char('#', 2)

    def test_shift_char_string(self):
        """Test shift_char function with a string"""
        with self.assertRaises(TypeError):
            helper_functions.shift_char('tf', 2)

    def test_frequency_analysis_lowercase_string(self):
        """test frequency_analysis function with a lowercase string"""
        frequencies = helper_functions.frequency_analysis(self.string_without_spaces)
        self._assert_letter_frequencies(frequencies)

    def test_frequency_analysis_empty_string(self):
        """test frequency_analysis function with an empty string"""
        frequencies = helper_functions.frequency_analysis("")
        self.assertTrue(len(frequencies) == 0)

    def test_frequency_analysis_string_with_spaces(self):
        """test frequency_analysis function with a lowercase string with spaces"""
        frequencies = helper_functions.frequency_analysis(self.string_with_spaces)
        self._assert_letter_frequencies(frequencies)

    def test_frequency_analysis_uppercase_string(self):
        """test frequency_analysis function with a lowercase string"""
        frequencies = helper_functions.frequency_analysis(self.string_without_spaces.upper())
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
