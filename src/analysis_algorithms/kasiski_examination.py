"""Performs Kasiski examination"""
from math import gcd
from collections import Counter

def _repeated_substring_distance(text):
    # Create a dictionary with 3grams as keys and a list of starting indices of the 3-gram as values
    threegram_indices = {}
    for i in range(0, len(text)-2): # Loop over the text
        sub_string = text[i:i+3] #Get substring of length 3 starting at index i
        if sub_string in threegram_indices:
            threegram_indices[sub_string].append(i)
        else:
            threegram_indices[sub_string]=[i]
    distances = []
    for indices in threegram_indices.values():
        for i in range(len(indices)-1):
            for j in range(i+1, len(indices)):
                distances.append(indices[j]-indices[i])
    return distances

# Get all the factors of a number
def _get_factors(num):
    factors = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            # Add the factors to the list
            factors.extend([i, num//i])
    return factors

#Calculate the key length based on the factors of all the distances between repeated substrings
def _get_possible_key_length(distances):
    if len(distances) == 0:
        raise ValueError
    frequencies = Counter()
    # Loop over the distances between the repeated 3grams and calculate factors- likely key lengths
    for i in distances:
        factors = _get_factors(i)
        frequencies.update(factors)
    # Remove 2 as it sometimes causes the result to be multiplied by 2 unnecessarily
    del frequencies[2]
    max_value = frequencies.most_common(1)[0][1]
    possible_key_lengths = []
    for key, value in frequencies.items():
        if value >= max_value * 0.75:
            possible_key_lengths.append(key)
    return possible_key_lengths

# Get the length of the key by finding the lowest common multiple of all possible key lengths
def _get_key_length(possible_key_lengths):
    if len(possible_key_lengths) == 0:
        raise ValueError
    lcm = 1
    for i in possible_key_lengths:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def run_kasiski_examination(ciphertext):
    """
    Perform Kasiski Examination
    Calculate the key length based on the factors of all the distances between repeated substrings
        Parameters:
            ciphertext (string): The ciphertext to be analysed
        Returns:
            key_length (int): The likely length of the key
    """
    distances = _repeated_substring_distance(ciphertext)
    possible_key_lengths = _get_possible_key_length(distances)
    key_length = _get_key_length(possible_key_lengths)
    return key_length
