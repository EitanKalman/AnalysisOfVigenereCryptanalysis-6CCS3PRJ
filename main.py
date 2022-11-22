import time
from random import randint
from helper_functions import vigenere
from IOC_Working import run_IOC_attack
from Shifted_Text_Coincidence import run_shifted_text_attack
from Kasiski import run_kasiski_attack
from Key_Crack_From_Key_Length import get_key


def read_file(file_to_open):
    try:
        with open(f"texts/{file_to_open}", 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return ""


def time_attack(ciphertext, attack):
    start_time = time.time()
    calculated_key_length = attack(ciphertext)
    end_time = time.time()
    print(calculated_key_length)
    return(end_time-start_time)

def average_time(ciphertexts, attack):
    total_time = 0
    for text in ciphertexts:
        total_time += time_attack(text, attack)
    total_time /= len(ciphertexts)
    return total_time


def main_temp():
    key_length = randint(3,20)
    key = ""
    for i in range(0, key_length):
        val = randint(97, 122)
        key +=chr(val)
    key = "oxhagi"
    print(key, len(key))
    plaintext = read_file("Dracula.txt")
    # plaintext = read_file("Two_Towers_Ch_1.txt")
    # plaintext = read_file("Return_of_the_King_Ch_1.txt")
    # plaintext = read_file("Hobbit_Ch_1.txt")

    ciphertext = vigenere(plaintext, key, True)

    start_time = time.time()
    run_IOC_attack(ciphertext)
    end_time = time.time()
    print(f"time: {end_time-start_time}")


def main():
    keys = []
    for i in range(0, 10):
        key_length = randint(3,20)
        key = ""
        for i in range(0, key_length):
            val = randint(97, 122)
            key +=chr(val)
        keys.append(key)
    string = ""
    for i in keys:
        string += f"{len(i)}, "
    print(string)
    print(keys)
    # attacks = [run_IOC_attack, run_shifted_text_attack, run_kasiski_attack]
    attacks = [run_kasiski_attack]
    files = [
        "Two_Cities_Ch_1.txt",
        "Two_Towers_Ch_1.txt",
        "HHGTTG_Ch_1.txt",
        "Hobbit_Ch_1.txt",
        "Fellowship_Ch_1.txt",
        "Return_of_the_King_Ch_1.txt"
        # ,
        # "Alice.txt",
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
            average_runtime = average_time(text, attack)
            print(f"{attack.__name__}, ciphertext length: {char_count}, time: {average_runtime}")


if __name__ == "__main__":
    main()
