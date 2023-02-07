"""Performs index of coincidence analysis on split ciphertext to calculate the key length"""
from collections import Counter
from math import gcd
try:
    from helper_functions import split
except ModuleNotFoundError:
    from src.helper_functions import split


# Calculates the Index of Coincidence for a given text
def _calculate_text_ioc(text):
    text = text.lower()
    length = len(text)
    # Get the frequency analysis for the text
    map_of_frequencies = Counter(text)
    ioc = 0
    for value in map_of_frequencies.values():
        ioc = ioc + (value * (value-1))/(length*(length-1))
    return ioc

# Calculate the index of coincidence for a ciphertext that has been split into n parts by
# calculating the index of coincidence for each part and then averaging
def _calculate_ioc_average(split_ciphertext):
    total = 0
    for sub_text in split_ciphertext:
        index_of_coincidence = _calculate_text_ioc(sub_text)
        total += index_of_coincidence
    return total/len(split_ciphertext)

def run_ioc_analysis(ciphertext):
    """
    Calculates a probable key length using index of coincidence analysis
        Parameters:
            ciphertext (string): The ciphertext to be analysed
        Returns:
            likely_key_length (int): The likely length of the key
    """
    possible_ley_lengths = []
    # Split the ciphertext
    for i in range(2, 20):
        # Split the ciphertext into i parts and calculate the index of coincidence for the split
        split_text = split(ciphertext, i)
        ioc_average = _calculate_ioc_average(split_text)
        # If this split has an ioc close to English, add it to possible key length candidates
        if abs(ioc_average - 0.065) < 0.005:
            possible_ley_lengths.append(i)
    # Reduce the list of possible keys lengths to the greatest common divisor and return
    return gcd(*possible_ley_lengths)
