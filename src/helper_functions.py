"""Provides various functions used in the program"""
from collections import Counter

def vigenere(text, key, encrypt = True):
    """
    Encrypt/ decrypt a message using the Vigenere cipher
        Parameters:
            text (string): The message to be encrypted/ decrypted
            key (string): The key to be used
            encrypt (boolean): True when encrypting, False when decrypting
        Returns:
            text (string): The encrypted/ decrypted message
        Raises:
            AssertionError: If text or key contain characters that aren't letters
    """
    text = text.replace(" ", "")
    key = key.replace(" ", "")
    key = key.lower()
    assert key.isalpha()
    output = ""
    key_length = len(key)
    for idx, char in enumerate(text):
        mod = idx % key_length
        shift = ord(key[mod]) - 97
        if not encrypt:
            shift = -shift
        output += shift_char(char, shift)
    return output

def split(text, num):
    """
    Splits a string into multiple substrings based on a provided number- num
    Each substring is made up of every nth character.
    i.e 1st substring is 1st, (n+1)th, (2n+1)th; 2nd substring is 2nd, (n+2)th, (2n+2)th etc
        Parameters:
            text (string): The text to be split
            num (int): The number of sub-texts the text should be split in to
        Returns:
            sub_strings (list[string]): A list of strings, containing the splits
        Raises:
            ValueError: If num isn't greater than 0
            TypeError: If num isn't an integer
    """
    if num < 1:
        raise ValueError("num must be greater than 0")
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    sub_strings = []
    for _ in range(0, num):
        sub_strings.append("")
    for idx, char in enumerate(text):
        mod = idx % num
        sub_strings[mod] += char
    return sub_strings

def shift_char(char, shift):
    """
    Shifts a character based on a given shift
        Parameters:
            char (char): The character to be shifted (will be converted to lowercase)
            shift (int): The number of places to shift
        Returns:
            char (char): The character resulting from the shift
        Raises:
            TypeError: If shift isn't an integer
            AssertionError: If char isn't a letter character
            TypeError: If char isn't a single character
    """
    assert char.isalpha()
    if len(char) != 1:
        raise TypeError("char must be a single character")
    char = char.lower()
    val = ord(char)
    val += shift
    while val > 122:
        val -= 26
    while val < 97:
        val +=26
    return chr(val)

def frequency_analysis(string):
    """
    Performs frequency analysis of a string
        Parameters:
            string (string): The string to be analysed (will be converted to lowercase)
        Returns:
            counter (Counter): A Counter object that contains the frequencies of all letters
    """
    string = string.lower()
    string = string.replace(" ", "")
    letter_counter = Counter(string)
    return letter_counter
