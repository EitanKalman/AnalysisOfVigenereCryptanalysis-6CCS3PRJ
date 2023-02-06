"""Calculate the key for a ciphertext given the key length"""
try:
    from helper_functions import split, shift_char, frequency_analysis, normalise
except ModuleNotFoundError:
    from src.helper_functions import split, shift_char, frequency_analysis, normalise


# Dictionary containing the frequencies of all letters in English
english_letter_frequencies = {
    'a':0.08672083734,
    'b':0.0148505829,
    'c':0.03424333016,
    'd':0.0390381717,
    'e':0.1215476703,
    'f':0.02302089594,
    'g':0.01945129235,
    'h':0.04745351843,
    'i':0.0753189498,
    'j':0.00187051741,
    'k':0.00600429726,
    'l':0.04236963167,
    'm':0.02646728388,
    'n':0.07337440171,
    'o':0.07377156799,
    'p':0.02124003257,
    'q':0.00109944054,
    'r':0.06624957169,
    's':0.06633069973,
    't':0.08598064819,
    'u':0.02690630195,
    'v':0.01060964146,
    'w':0.01672883441,
    'x':0.00201884315,
    'y':0.01550863958,
    'z':0.0013238847
}

# Calculate the cumulative chi squared value for all characters in a given text
def _chi_squared(letter_frequencies, text_length):
    total = 0
    # This loop runs 26 times are there are always at most 26 key-value pairs
    for key, value in letter_frequencies.items():
        probability = english_letter_frequencies[key]
        expected_count = probability * text_length
        total += ((value - expected_count)**2)/expected_count
    return total

# Shifts all characters in a text left by the desired number of places
def _shift_left(text, shift):
    if shift < 1:
        raise ValueError("shift must be greater than 0")
    output = ""
    for char in text:
        new_char = shift_char(char, -shift)
        output += new_char
    return output

def get_key(ciphertext, key_length):
    """
    Calculates the key for a ciphertext given the key length
        Parameters:
            ciphertext (string): The ciphertext
            key_length (int): The length of the key
        Return:
            key (string): The calculated key
    """
    # Split the ciphertext into key_length many sub-strings
    split_text = split(ciphertext, key_length)
    key = ""
    # This loop combines with the loop that will be performed in _shift_left to be O(n)
    # as this loop runs k times (the number of elements in split_text- i.e. the key length), and
    # each string being looped over there has n/k chars (where n is the length of the ciphertext)
    for text in split_text:
        length = len(text)
        chi_values = []
        # For each possible shift calculate the cumulative chi squared value
        for i in range(0, 26):
            shift_text = _shift_left(text, i)
            frequencies = frequency_analysis(shift_text)
            chi = _chi_squared(frequencies, length)
            chi_values.append(chi)
        # Find the index of the smallest chi square value- the shift
        shift_number = chi_values.index(min(chi_values))
        # Convert the shift to a letter based using ascii
        shift_number = 97 + shift_number
        shift_number = normalise(shift_number)
        key += chr(shift_number)
    return key
