"""Main- the start point of the program"""
from time import perf_counter
from random import randint
from os import listdir
from re import compile as regex_compile
from helper_functions import vigenere
from analysis_algorithms.ioc_analysis import run_ioc_analysis
from analysis_algorithms.shifted_text_coincidence import run_shifted_text_analysis
from analysis_algorithms.kasiski_examination import run_kasiski_examination
from calculate_key import get_key


def read_file(file_to_open):
    """
    Opens a file and reads its contents
        Parameters:
            file_to_open (string): The name of the file to be opened
        Returns:
            text (string): The contents of the file, or an empty string if an error occurs
    """
    try:
        with open(f"texts/{file_to_open}", 'r', encoding="utf-8") as file:
            text = file.read()
            text = text.lower() 
            reg = regex_compile('[^a-z]')
            text = reg.sub("", text)
            return text
    except FileNotFoundError:
        return ""

def time_attack(ciphertext, attack):
    """
    Times how long a cryptographic algorithm takes on a given ciphertext
    Parameters:
        ciphertext (string): The ciphertext to be cryptanalysed
        attack (function): The cryptanalysis algorithm to be used
    Returns:
        time (float): The time it took for the algorithm itself to run
        time (float): The time is took for the algorithm and key calculation to run
        key (string): The calculated key for this ciphertext
    """
    start_time = perf_counter()
    calculated_key_length = attack(ciphertext)
    mid_point = perf_counter()
    key = get_key(ciphertext, calculated_key_length)
    end_time = perf_counter()
    return mid_point-start_time, end_time-mid_point, end_time-start_time, key

def calc_average_time(ciphertexts, attack):
    """
    Run a cryptanalysis algorithm on multiple ciphertexts and calculate the average time
    Parameters:
        ciphertexts (list[strings]): The list of ciphertexts to be analysed
        attack (function): The cryptanalysis algorithm to be used
    Returns:
        average_time (float): The average time across all ciphertexts (without key calculation)
        average_time (float): The average time across all ciphertexts (with key calculation)
        calculated_keys (list[string]): A list of the calculated keys for each ciphertext
    """
    total_time = 0
    total_time_key = 0
    total_time_full = 0
    calculated_keys = []
    # For each ciphertext time how long it takes to perform the analysis and the time to do the
    # analysis and calculate the key, as well as get the calculated key
    for text in ciphertexts:
        runtime, runtime_key, runtime_full, key = time_attack(text, attack)
        total_time += runtime
        total_time_key += runtime_key
        total_time_full += runtime_full
        calculated_keys.append(key)
    # Calculate the average time
    total_time /= len(ciphertexts)
    total_time_key /= len(ciphertexts)
    total_time_full /= len(ciphertexts)
    return total_time, total_time_key, total_time_full, calculated_keys

def _generate_keys():
    keys = []
    for _ in range(0, 10):
        key_length = randint(3,20)
        key = ""
        for _ in range(0, key_length):
            val = randint(97, 122)
            key +=chr(val)
        keys.append(key)
    return keys

def _load_plaintexts():
    all_files = listdir("texts/")
    txt_files = list(filter(lambda x: x[-4:] == '.txt', all_files))
    plaintexts = []
    for file in txt_files:
        plaintext = read_file(file)
        if len(plaintext) > 0:
            plaintexts.append(plaintext)
    plaintexts.sort(key = len)
    return plaintexts

def _generate_ciphertexts(plaintexts, keys):
    all_ciphertexts = []
    for text in plaintexts:
        # For 1 plaintext, generate ciphertexts for all keys
        ciphertexts = []
        for key in keys:
            ciphertexts.append(vigenere(text, key, True))
        all_ciphertexts.append(ciphertexts)
    return all_ciphertexts

def main():
    """The main method- entry point of the program"""
    print("Generating keys")
    keys = _generate_keys()
    print(f"keys are: {keys}")
    print("Loading plaintexts")
    plaintexts = _load_plaintexts()
    print("Generating ciphertexts")
    all_ciphertexts = _generate_ciphertexts(plaintexts, keys)
    print("Ciphertexts Generated \nRunning cryptanalysis algorithms")

    algorithms = [run_ioc_analysis, run_shifted_text_analysis, run_kasiski_examination]

    # Run all algorithms on all plaintexts and print the average time
    for algo in algorithms:
        for text in all_ciphertexts:
            char_count = len(text[0])
            average_runtime, average_runtime_key, average_runtime_full, calc_keys = calc_average_time(text, algo)
            print(f"{algo.__name__}, ciphertext length:{char_count}, time w/o key:{average_runtime}, time for key:{average_runtime_key}, time w/ key:{average_runtime_full}")
            # Check that the calculated keys are correct
            if calc_keys != keys:
                print("calculated keys aren't correct")


if __name__ == "__main__":
    main()
