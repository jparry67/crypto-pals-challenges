"""
Set 1: Basics - Challenge 2: Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179

Example usage:
python chal2.py 1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965
Output:
746865206b696420646f6e277420706c6179
"""

from argparse import ArgumentParser
from crypto_utils import validate_hex, hex_char_to_int, hex_to_bytes, xor_bytearrays

def validate_lengths(first_buf, second_buf):
  if len(first_buf) != len(second_buf):
    raise ValueError("buffer strings must be the same length")

def int_to_hex_char(int):
  if int < 0 or int > 15:
    raise ValueError("unexpected int for hex char")
  if int < 10:
    return str(int)
  return chr(int + 88)

def bytes_to_hex(bytes):
  hex_str = ''
  for byte in bytes:
    first_hex_int = byte >> 4
    second_hex_int = byte & 15
    hex_str += int_to_hex_char(first_hex_int) + int_to_hex_char(second_hex_int)
  return hex_str

parser = ArgumentParser()
parser.add_argument("first_buf", help="first buffer to xor")
parser.add_argument("second_buf", help="second buffer to xor")
args = parser.parse_args()
first_buf = args.first_buf
second_buf = args.second_buf

validate_hex(first_buf)
validate_hex(second_buf)
validate_lengths(first_buf, second_buf)
first_bytes = hex_to_bytes(first_buf)
second_bytes = hex_to_bytes(second_buf)
xor_bytes = xor_bytearrays(first_bytes, second_bytes)
xor_hex = bytes_to_hex(xor_bytes)
print(xor_hex)