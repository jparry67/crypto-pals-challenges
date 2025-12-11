"""
Set 1: Basics - Challenge 4: Detect single-character XOR

One of the 60-character strings in this file (saved here as input.txt) has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)

Example usage:
python chal4.py chal4_input.txt
Output:
Best match: Now that the party is jumping
"""

from argparse import ArgumentParser
from crypto_utils import validate_hex, hex_char_to_int, hex_to_bytes, xor_bytearrays, generate_xor_options, score_string_validity

parser = ArgumentParser()
parser.add_argument("file", help="the file with the list of hex encoded strings to check")
args = parser.parse_args()
file_name = args.file

file = open(file_name, "r")

best_matches = []
for line in file:
    line = line.strip()
    validate_hex(line)
    hex_bytes = hex_to_bytes(line)
    xor_options = generate_xor_options(len(line))
    option_scores = []
    for option in xor_options:
        xor_bytes = xor_bytearrays(hex_bytes, option)
        try:
            decoded_string = xor_bytes.decode('utf-8')
            option_score = score_string_validity(decoded_string)
            option_scores.append((option_score, decoded_string))
        except UnicodeDecodeError:
            pass
    option_scores.sort(reverse=True)
    if len(option_scores):
        best_matches.append(option_scores[0])
best_matches.sort(reverse=True)
print('Best match:', best_matches[0][1])
file.close()