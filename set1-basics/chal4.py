"""
Set 1: Basics - Challenge 4: Detect single-character XOR

One of the 60-character strings in this file (saved here as input.txt) has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)

Example usage:
python chal4.py chal4_input.txt
Output:

"""

from argparse import ArgumentParser
from crypto_utils import validate_hex, hex_char_to_int, hex_to_bytes, xor_bytearrays

