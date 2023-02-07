"""Provides various functions used in the program"""
def vigenere(text, key, encrypt):
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
    text = text.lower()
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
    val = normalise(val)
    return chr(val)

def normalise(num):
    """
    Keeps a number between 97 and 122 (the ascii values for 'a' and 'z')
        Parameters:
            num (int): An integer number
        Returns:
            num (int): The number once normalised
    """
    while num > 122:
        num -= 26
    while num < 97:
        num +=26
    return num
