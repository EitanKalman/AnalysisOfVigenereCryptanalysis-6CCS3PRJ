from math import gcd
from functools import reduce
from helper_functions import split, frequency_analysis

# Calculates the Index of Coincidence for a given text
def _calculate_text_IOC(text):
    length = len(text)
    # Get the frequency analysis for the text
    map_of_frequencies = frequency_analysis(text)
    sum = 0
    for value in map_of_frequencies.values():
        sum = sum + (value * (value-1))
    IOC = sum/(length*(length-1))
    return IOC

# Calculate the index of coincides for a ciphertext that has been split into n parts by
# calculating the index of coincidence for each part and then averaging
def _calculate_IOC_average(split_ciphertext):
    sum = 0
    for split in split_ciphertext:
        index_of_coincidence = _calculate_text_IOC(split)
        sum += index_of_coincidence
    return sum/len(split_ciphertext)

def run_IOC_attack(ciphertext):
    possible_ley_lengths = []
    # Split the ciphertext 
    for i in range(2, 20):
        # Split the ciphertext into i parts and calculate the index of coincidence for the split
        split_text = split(ciphertext, i)
        IOC_average = _calculate_IOC_average(split_text)
        # If this split has an index of coincidence close to English, add it to possible key length candidates
        if abs(IOC_average - 0.067) < 0.01:
            possible_ley_lengths.append(i)
    return reduce(gcd, possible_ley_lengths)
