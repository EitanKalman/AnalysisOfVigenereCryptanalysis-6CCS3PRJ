"""Performs shifted text coincidence analysis"""

# Pads the input string with the desired number of spaces on the left
# Effectively shifts the input string left by n spaces
def _add_left_padding(text, num):
    if num < 0:
        raise ValueError("num must be greater than 0")
    return " "*num + text

# Compares 2 texts (the original and a shifted version) to find how many coincidences there are
# between the 2 texts. Coincidences are defined as the same character at the same index
def _compare(text1, text2):
    coincidence = 0
    for char1, char2 in zip(text1, text2):
        if char1 == char2:
            coincidence+=1
    return coincidence

def run_shifted_text_analysis(ciphertext):
    """
    Calculates a probable key length using shifted text analysis
        Parameters:
            ciphertext (string): The ciphertext to be analysed
        Returns:
            likely_key_length (int): The likely length of the key
    """
    possible_key_lengths = []
    # Created shifted versions of the ciphertext
    for i in range(2, 21):
        text = _add_left_padding(ciphertext, i)
        # Get the number of coincidences for this shifted version
        coincidence = _compare(ciphertext, text)
        # If the number of coincidences is above the threshold include it as a possible key length
        if coincidence>(len(ciphertext)/18):
            possible_key_lengths.append(i)
    key_length = min(possible_key_lengths)
    return key_length
