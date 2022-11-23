"""Provides various functions used in the program"""
from collections import Counter

def vigenere(text, key, encrypt):
    """
    Encrypt/ decrypt a message using the Vigenere cipher
        Paramaters:
            text (string): the message to be encrypted/ decrypted
            key (string): the key to be used
            encrypt (boolean): True when encrypting, false when decrypting
    """
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
    """
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
            char (char): The character to be shifted
            shift (int): The number of places to shift
        Returns:
            char (char): The character resulting from the shift
    """
    val = ord(char)
    val += shift
    if val > 122:
        val -= 26
    if val < 97:
        val +=26
    return chr(val)

# def frequency_analysis(text):
#     frequencies = {}
#     for char in text:
#         if char in frequencies:
#             frequencies[char] = frequencies[char] + 1
#         else:
#             frequencies[char] = 1
#     return frequencies

def frequency_analysis(string):
    """
    Performs frequency analysis of a string
        Parameters:
            string (string): The string to be analysed
        Returns:
            counter (Counter): A Counter object that contains the frequencies of all letters
    """
    letter_counter = Counter(string)
    return letter_counter
