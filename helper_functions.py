from collections import Counter

# Encrypt/ decrypt a message using the Vigenere cipher
# Params: text- the message to be encrypted/ decrypted, key- the Vigenere key, encrypt- True when encrypting, false when decrypting 
def vigenere(text, key, encrypt):
    output = ""
    key_length = len(key)
    for i in range(0, len(text)):
        mod = i % key_length
        shift = ord(key[mod])-97
        if not encrypt:
            shift = -shift
        output += shift_char(text[i], shift)
    return output

# Splits a string into multiple substrings based on a provided number- num
# Each substring is made up of every nth character.
# i.e 1st substring is 1st, (n+1)th, (2n+1)th; 2nd substring is 2nd, (n+2)th, (2n+2)th etc
def split(text, num):
    subStrings = []
    for i in range(0, num):
        subStrings.append("")
    for i in range(0, len(text)):
        mod = i % num
        subStrings[mod] += text[i]
    return subStrings

# Shifts a character based on a given shift
def shift_char(char, shift):
    val = ord(char)
    val += shift
    if val > 122:
          val -= 26
    if val < 97:
        val +=26
    return chr(val)

# def frequency_analysis(text):
#     frequencies = {}
#     for char in text:
#         if char in frequencies:
#             frequencies[char] = frequencies[char] + 1
#         else:
#             frequencies[char] = 1
#     return frequencies

# Creates a Counter object that contains the frequency of all letters in a string
def frequency_analysis(string):
    letter_counter = Counter(string)
    return letter_counter
