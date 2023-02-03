from unittest import TestCase
from src.helper_functions import shift_char, frequency_analysis


class TestShiftChar(TestCase):

    def test_valid_char_with_positive_shift(self):
        new_char = shift_char('g', 1)
        self.assertEqual(new_char, 'h')

    def test_valid_lower_boundary_char_with_positive_shift(self):
        new_char = shift_char('a', 1)
        self.assertEqual(new_char, 'b')

    def test_valid_upper_boundary_char_with_positive_shift(self):
        new_char = shift_char('z', 1)
        self.assertEqual(new_char, 'a')

    def test_valid_char_with_negative_shift(self):
        new_char = shift_char('g', -1)
        self.assertEqual(new_char, 'f')

    def test_valid_lower_boundary_char_with_negative_shift(self):
        new_char = shift_char('a', -1)
        self.assertEqual(new_char, 'z')

    def test_valid_upper_boundary_char_with_negative_shift(self):
        new_char = shift_char('z', -1)
        self.assertEqual(new_char, 'y')

    def test_valid_char_with_large_positive_shift(self):
        new_char = shift_char('g', 100)
        self.assertEqual(new_char, 'c')

    def test_valid_char_with_large_negative_shift(self):
        new_char = shift_char('t', -100)
        self.assertEqual(new_char, 'x')


class TestFrequencyAnalysis(TestCase):

    def setUp(self):
        self.valid_string = "teststring"

    def test_valid_string(self):
        frequencies = frequency_analysis(self.valid_string)
        self.assertFalse(len(frequencies) == 0)
        self.assertEqual(frequencies['t'], 3)

    def test_empty_string(self):
        frequencies = frequency_analysis("")
        self.assertTrue(len(frequencies) == 0)

    def test_string_with_spaces(self):
        frequencies = frequency_analysis("test string")
        self.assertFalse(len(frequencies) == 0)
        self.assertEqual(frequencies['t'], 3)
        self.assertEqual(frequencies[' '], 1)
