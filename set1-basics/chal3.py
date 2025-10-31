"""
Set 1: Basics - Challenge 3: Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Example usage:
python chal3.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
Output:
Best match: Cooking MC's like a pound of bacon
"""

from argparse import ArgumentParser
from crypto_utils import validate_hex, hex_char_to_int, hex_to_bytes, xor_bytearrays

def generate_xor_options(xor_length):
    xor_options = []
    # uppercase letters
    for i in range(65, 91):
        xor_options.append(bytearray([i]) * xor_length)
    # lowercase letters
    for i in range(97, 123):
        xor_options.append(bytearray([i]) * xor_length)
    return xor_options

def score_string_validity(string):
    score = 0
    for char in string:
        if char in "aeiouAEIOU":
            score += 3
        elif char.isalpha():
            score += 2
        elif char in "\"'{}()_-,.!":
            score += 1
    return score

parser = ArgumentParser()
parser.add_argument("hex", help="the hex encoded string to decode")
args = parser.parse_args()
hex_str = args.hex

validate_hex(hex_str)
hex_bytes = hex_to_bytes(hex_str)
xor_options = generate_xor_options(len(hex_str))
option_scores = []
for option in xor_options:
    xor_bytes = xor_bytearrays(hex_bytes, option)
    option_score = score_string_validity(xor_bytes.decode('utf-8'))
    print(option_score)
    option_scores.append((option_score, xor_bytes.decode('utf-8')))
option_scores.sort(reverse=True)

print('Best match:', option_scores[0][1])