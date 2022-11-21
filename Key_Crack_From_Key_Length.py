from helper_functions import split, shift_char, frequency_analysis

# Dictionary containing the frequencies of all letters in English
english_letter_frequencies = {
    'a':0.08167,
    'b':0.01492,
    'c':0.02782,
    'd':0.04253,
    'e':0.12702,
    'f':0.02228,
    'g':0.02015,
    'h':0.06094,
    'i':0.06966,
    'j':0.00153,
    'k':0.00772,
    'l':0.04025,
    'm':0.02406,
    'n':0.06749,
    'o':0.07507,
    'p':0.01929,
    'q':0.00095,
    'r':0.05987,
    's':0.06327,
    't':0.09056,
    'u':0.02758,
    'v':0.00978,
    'w':0.02360,
    'x':0.00150,
    'y':0.01974,
    'z':0.00074
}

# def frequency_analysis(text):
#     frequencies = {}
#     for char in text:
#         if char in frequencies:
#             frequencies[char] = frequencies[char] + 1
#         else:
#             frequencies[char] = 1
#     return frequencies

# Calculate the cumulative chi squared value for all characters in a given text
def _chi_squared(letter_frequencies, text_length):
    sum = 0
    # This loop runs 26 times are there are always at most 26 key-value pairs
    for key, value in letter_frequencies.items():
        probability = english_letter_frequencies[key]
        expectedCount = probability * text_length
        sum += ((value - expectedCount)**2)/expectedCount
    return sum

# Shifts all characters in a text left by the desired number of places
def _shift_left(text, shift):
    output = ""
    for char in text:
        new_char = shift_char(char, -shift)
        output += new_char
    return output

# Calculates the key for a ciphertext given the key length
def get_key(ciphertext, key_length):
    # Split the ciphertext into key_length many sub-strings
    split_text = split(ciphertext, key_length)
    key = ""
    # This loop combines with the loop that will be performed in _shift_left to be O(n)
    # as this loop runs k times (the number of elements in split_text- i.e. the key length),
    # and each string being looped over there has n/k characters (where n is the length of the ciphertext)
    for text in split_text:
        length = len(text)
        chi_values = []
        # For each possible shift calculate the cumulative chi squared value
        for i in range(0, 26):
            shiftText = _shift_left(text, i)
            frequencies = frequency_analysis(shiftText)
            chi = _chi_squared(frequencies, length)
            chi_values.append(chi)
        # Find the index of the smallest chi square value- the shift
        shift_number = chi_values.index(min(chi_values))
        # Convert the shift to a letter based using ascii
        shift_number = 97 + shift_number
        if shift_number > 122:
            shift_number -= 26
        if shift_number < 97:
            shift_number +=26
        key += chr(shift_number)
    return key

