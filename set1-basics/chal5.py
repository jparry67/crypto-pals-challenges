"""
Set 1: Basics - Challenge 5: Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.

Example usage:
python chal5.py chal5_input.txt ICE
Output:
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""

from argparse import ArgumentParser
from crypto_utils import int_to_hex_chars

parser = ArgumentParser()
parser.add_argument("input_file", help="the file with the text to encrypt")
parser.add_argument("key", help="the key used to encrypt the text")
args = parser.parse_args()
file_name = args.input_file
key = args.key

input_file = open(file_name, "r")
cleartext = input_file.read()
hex_result = []
for i in range(len(cleartext)):
    cleartext_val = ord(cleartext[i])
    key_val = ord(key[i % len(key)])
    xord = cleartext_val ^ key_val
    hex_result.append(int_to_hex_chars(cleartext_val ^ key_val))
print(''.join(hex_result))