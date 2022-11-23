"""Main- the start point of the program"""
import time
from random import randint
from helper_functions import vigenere
from ioc_examination import run_ioc_attack
from shifted_text_coincidence import run_shifted_text_attack
from kasiski_examination import run_kasiski_attack
from Key_Crack_From_Key_Length import get_key


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
            return text
    except FileNotFoundError:
        return ""

def time_attack(ciphertext, attack):
    """
    Times how long it takes a cryptographic algorithm takes on a given ciphertext
    Parameters:
        ciphertext (string): The ciphertext to be cryptanalysed
        attack (function): The cryptanalysis algorithm to be used
    Returns:
        time (float): The time it took for the algorithm to run
    """
    start_time = time.time()
    calculated_key_length = attack(ciphertext)
    end_time = time.time()
    print(calculated_key_length)
    return end_time-start_time

def calculate_average_time(ciphertexts, attack):
    """
    Run a cryptanalysis algorithm on multiple ciphertexts and calculate the average time
    Parameters:
        ciphertexts (list[strings]): The list of ciphertexts to be analysed
        attack (function): The cryptanalysis algorithm to be used
    Returns:
        average_time (float): The average time across all ciphertexts
    """
    total_time = 0
    for text in ciphertexts:
        total_time += time_attack(text, attack)
    total_time /= len(ciphertexts)
    return total_time


# def main_temp():
#     key_length = randint(3,20)
#     key = ""
#     for i in range(0, key_length):
#         val = randint(97, 122)
#         key +=chr(val)
#     key = "oxhagi"
#     print(key, len(key))
#     plaintext = read_file("Dracula.txt")
#     # plaintext = read_file("Two_Towers_Ch_1.txt")
#     # plaintext = read_file("Return_of_the_King_Ch_1.txt")
#     # plaintext = read_file("Hobbit_Ch_1.txt")

#     ciphertext = vigenere(plaintext, key, True)

#     start_time = time.time()
#     run_ioc_attack(ciphertext)
#     end_time = time.time()
#     print(f"time: {end_time-start_time}")

def main():
    """The main method- entry point of the program"""
    keys = []
    for i in range(0, 1):
        key_length = randint(3,20)
        key = ""
        for i in range(0, key_length):
            val = randint(97, 122)
            key +=chr(val)
        keys.append(key)
    string = "keys lengths: "
    for i in keys:
        string += f"{len(i)}, "
    print(string)
    # print(keys)
    attacks = [run_ioc_attack, run_shifted_text_attack, run_kasiski_attack]
    # attacks = [run_kasiski_attack]
    files = [
        "Two_Cities_Ch_1.txt",
        "Two_Towers_Ch_1.txt",
        "HHGTTG_Ch_1.txt",
        "Jekyll_and_Hyde.txt",
        "Hobbit_Ch_1.txt",
        "Fellowship_Ch_1.txt",
        "Return_of_the_King_Ch_1.txt",
        "Tom_Sawyer.txt"
        # ,
        # "Alice.txt",
        # "A_Room_With_A_View.txt",
        # "Frankenstein.txt",
        # "Sherlock_Holmes.txt",
        # "Dracula.txt",
        # "Moby_Dick.txt"
        ]
    texts = []
    for file in files:
        texts.append(read_file(file))

    all_ciphertexts = []
    for text in texts:
        ciphertexts = []
        for key in keys:
            ciphertexts.append(vigenere(text, key, True))
        all_ciphertexts.append(ciphertexts)

    for attack in attacks:
        for text in all_ciphertexts:
            char_count = len(text[0])
            average_runtime = calculate_average_time(text, attack)
            print(f"{attack.__name__}, ciphertext length: {char_count}, time: {average_runtime}")


if __name__ == "__main__":
    main()
