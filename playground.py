from Kasiski import _repeated_substring_distance, _get_factors
from main import read_file
from helper_functions import vigenere
from collections import Counter
import time
from random import randint

def get_all_factors(distances):
    all_factors = []
    for i in distances:
        factors = _get_factors(i)
        all_factors.extend(factors)
    print(f"factors calculated: {len(all_factors)}")
    return all_factors

def get_factor_frequencies_dict(all_factors):
	# Count the frequencies of all factors
    frequencies = {}
    for factor in all_factors:
        if factor in frequencies:
            frequencies[factor] += 1
        else:
            frequencies[factor] = 1
    return frequencies

def get_factor_frequencies_counter(all_factors):
	# Count the frequencies of all factors
    frequencies = Counter(all_factors)	
    return frequencies

def main():
    plaintext = read_file("HHGTTG_Ch_1.txt")
    print(len(plaintext))
    # plaintext = read_file("Fellowship_Ch_1.txt")
    # key_length = randint(3, 20)
    # key = ""
    # for i in range(0, key_length):
    #     val = randint(97, 122)
    #     key +=chr(val)
    # print(key, len(key))
    # ciphertext = vigenere(plaintext, key, True)
    # print("ciphertext generated")
    # distances = _repeated_substring_distance(ciphertext)
    # print(f"distances calculated: {len(distances)}")

    # all_factors = get_all_factors(distances)

    # start_time = time.time()
    # dict = get_factor_frequencies_dict(all_factors)
    # end_time = time.time()
    # print(f"dict time: {end_time-start_time}")

    # start_time = time.time()
    # counter = get_factor_frequencies_counter(all_factors)
    # end_time = time.time()
    # print(f"counter time: {end_time-start_time}")


    # for key, value in dict.items():
    #     if counter[key] != value:
    #         print(False) 
    

if __name__ == "__main__":
    main()