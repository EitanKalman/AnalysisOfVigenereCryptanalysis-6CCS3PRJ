"""Performs shifted text coincidence analysis"""
from math import gcd
from functools import reduce

# Pads the input string with the desired number of spaces on the left
# Effectively shifts the input string left by n spaces
def _add_left_padding(text, num):
    return " "*num + text

# Compares 2 texts (the original and a shifted version) to find how many coincidences there are
# between the 2 texts. Coincidences are defined as the same character at the same index
def _compare(text1, text2):
    coincidence = 0
    for char1, char2 in zip(text1, text2):
        if char1 == char2:
            coincidence+=1
    return coincidence

def run_shifted_text_analysis(ciphertext):
    """
    Calculates a probable key length using shifted text analysis
        Parameters:
            ciphertext (string): The ciphertext to be analysed
        Returns:
            likely_key_length (int): The likely length of the key
    """
    texts = []
    # Created shifted versions of the ciphertext
    for i in range(3, 21):
        text = _add_left_padding(ciphertext, i)
        texts.append(text)
    coincidences = []
    # Get the number of coincidences for each shifted version
    for i in texts:
        coincidence = _compare(ciphertext, i)
        coincidences.append(coincidence)
    # Filter out those shifts with the highest number of coincidences
    possible_key_lengths = []
    for idx, coincidence in enumerate(coincidences):
        if coincidence>(len(ciphertext)/18):
            possible_key_lengths.append(idx+3)
    # Reduce the list of possible keys lengths to the greatest common divisor and return
    return reduce(gcd, possible_key_lengths)
