"""Main- the start point of the program"""
from time import perf_counter
from random import randint
from os import listdir
from re import compile as regex_compile
from src.helper_functions import vigenere
from src.analysis_algorithms.ioc_analysis import run_ioc_analysis
from src.analysis_algorithms.shifted_text_coincidence import run_shifted_text_analysis
from src.analysis_algorithms.kasiski_examination import run_kasiski_examination
from src.calculate_key import get_key

def _read_file(file_to_open):
    try:
        with open(f"texts/{file_to_open}", 'r', encoding="utf-8") as file:
            text = file.read()
            text = text.lower()
            reg = regex_compile('[^a-z]')
            text = reg.sub("", text)
            return text
    except FileNotFoundError:
        return ""

def _time_attack(ciphertext, attack):
    start_time = perf_counter()
    calculated_key_length = attack(ciphertext)
    mid_point = perf_counter()
    key = get_key(ciphertext, calculated_key_length)
    end_time = perf_counter()
    return mid_point-start_time, end_time-mid_point, end_time-start_time, key

def _calc_average_time(ciphertexts, attack):
    total_time = 0
    total_time_key = 0
    total_time_full = 0
    calculated_keys = []
    # For each ciphertext time how long it takes to perform the analysis and the time to do the
    # analysis and calculate the key, as well as get the calculated key
    for text in ciphertexts:
        runtime, runtime_key, runtime_full, key = _time_attack(text, attack)
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
        plaintext = _read_file(file)
        if len(plaintext) > 0:
            plaintexts.append(plaintext)
    plaintexts.sort(key = len)
    return plaintexts

def _generate_ciphertexts(plaintexts, keys):
    all_ciphertexts = []
    if len(plaintexts) < 1:
        raise ValueError("plaintexts can't be empty")
    if len(keys) < 1:
        raise ValueError("keys can't be empty")
    for text in plaintexts:
        # For 1 plaintext, generate ciphertexts for all keys
        ciphertexts = []
        for key in keys:
            ciphertexts.append(vigenere(text, key, True))
        all_ciphertexts.append(ciphertexts)
    return all_ciphertexts

def run_analysis():
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
            average_runtime, average_runtime_key, average_runtime_full, calc_keys = _calc_average_time(text, algo)
            print(f"{algo.__name__}, ciphertext length:{char_count}, time w/o key:{average_runtime}, time for key:{average_runtime_key}, time w/ key:{average_runtime_full}")
            # Check that the calculated keys are correct
            if calc_keys != keys:
                print("calculated keys aren't correct")
