"""Performs Kasiski examination"""
from math import gcd
from collections import Counter

# Get distances between repeated substrings of length 3
# OLD VERSION- takes over 3 mins on laptop
def _repeated_substring_distance_old(text):
    distances = []	# Used to store the distances between repeated substrings of length 3
    for i in range(0, len(text)-2): # Loop over the text
        sub_string = text[i:i+3]	#Get substring of length 3 starting at index i
        for j in range(i+1, len(text)-2):	#Loop over the remaining text
            if text[j:j+3] == sub_string:	#If the substring of length 3 starting at j matches the current substring
                distances.append(j-i)	#Add the distance between the starting positions to the list
    return distances


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
    # This triple nested for loop is only O(n*2) due to groupings
    # The first 2 loops combine to O(n) as there are y key-value pairs in the dictionary (where y
    # is the number of unique 3-grams), where the values are lists of numbers. Each list has on
    # average n/y elements, and the total number of elements in all lists is n.
    # The 3rd loop is O(n) as it's linear in n
    for indexes in threegram_indices.values():
        for i in range(len(indexes)-1):
            for j in range(i+1, len(indexes)):
                distances.append(indexes[j]-indexes[i])
    return distances

# Get all the factors of a number
def _get_factors(num):
    factors = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            # factors.append(i)
            # factors.append(number/i)
            factors.extend([i, num//i])
    return factors

#Calculate the key length based on the factors of all the distances between repeated substrings
def _get_possible_key_length(distances):
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
    lcm = 1
    for i in possible_key_lengths:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def run_kasiski_attack(ciphertext):
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