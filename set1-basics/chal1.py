"""
Set 1: Basics - Challenge 1: Convert hex to base64

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

Example usage:
python chal1.py 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Output:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""

from argparse import ArgumentParser
from crypto_utils import validate_hex, hex_char_to_int, hex_to_bytes

def byte_to_base64_char(byte):
  if byte < 26:
    return chr(byte + 65) # char between A-Z
  if byte < 52:
    return chr(byte + 71) # char between a-z
  if byte < 62:
    return str(byte - 52) # char between 0-9
  if byte == 62:
    return '+'
  if byte == 63:
    return '/'
  raise ValueError("unexpected byte value for base64")

def bytes_to_base64(bytes):
  base64_chars = []
  for i in range(0, len(bytes), 3):
    first_byte = bytes[i]
    second_byte = bytes[i+1] if len(bytes) > i+1 else 0
    third_byte = bytes[i+2] if len(bytes) > i+2 else 0

    # divide three 8-bit values into 4 6-bit values
    first_base64 = first_byte >> 2                                # first 6 bits of first byte
    second_base64 = ((first_byte & 3) << 4) + (second_byte >> 4)  # last 2 bits of first byte and first 4 bits of second byte
    third_base64 = ((second_byte & 15) << 2) + (third_byte >> 6)  # last 4 bits of second byte and first 2 bits of third byte
    fourth_base64 = third_byte & 63                               # last 6 bits of third byte

    base64_chars.append(byte_to_base64_char(first_base64))
    base64_chars.append(byte_to_base64_char(second_base64))
    base64_chars.append(byte_to_base64_char(third_base64) if len(bytes) > i+1 else '=')
    base64_chars.append(byte_to_base64_char(fourth_base64) if len(bytes) > i+2 else '=')

  return ''.join(base64_chars)

parser = ArgumentParser()
parser.add_argument("hex", help="hex string to convert to base64")
args = parser.parse_args()
hex = args.hex

validate_hex(hex)
bytes = hex_to_bytes(hex)
base64_str = bytes_to_base64(bytes)
print(base64_str)