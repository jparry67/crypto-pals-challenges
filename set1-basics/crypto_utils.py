def validate_hex(hex):
  if len(hex) % 2 == 1:
    raise ValueError("hex string must have an even number of characters")
  for char in hex:
    if not char.isnumeric() and not char in "abcdefABCDEF":
      raise ValueError("hex string must only contain numbers and letters A-F")

def hex_char_to_int(hex_char):
  if hex_char.isnumeric():
    return int(hex_char)
  return ord(hex_char.lower()) - 87

def int_to_hex_char(int_val):
  if int_val < 0 or int_val > 15:
    raise ValueError("unexpected int for hex char")
  if int_val < 10:
    return str(int_val)
  return chr(int_val + 87)

def int_to_hex_chars(int_val):
  if int_val < 0 or int_val > 255:
    raise ValueError("unexpected int for two digit hex char")
  first = int_to_hex_char(int_val // 16)
  second = int_to_hex_char(int_val % 16)
  print(int_val//16, first, int_val % 16, second)
  return first + second

def hex_to_bytes(hex):
  bytes = bytearray()
  for i in range(0, len(hex), 2):
    first_hex_int = hex_char_to_int(hex[i])
    second_hex_int = hex_char_to_int(hex[i+1])
    byte_int_val = (first_hex_int << 4) + second_hex_int
    bytes.append(byte_int_val)
  return bytes

def xor_bytearrays(first_bytes, second_bytes):
  xor_bytes = bytearray()
  for i in range(len(first_bytes)):
    xor_bytes.append(first_bytes[i] ^ second_bytes[i])
  return xor_bytes

def generate_xor_options(xor_length):
  xor_options = []
  # numbers
  for i in range(48, 58):
    xor_options.append(bytearray([i]) * xor_length)
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
      score += 4
      if char.islower():
        score += 1
    elif char.isalpha():
      score += 3
      if char.islower():
        score += 1
    elif char.isspace():
      score += 2
    elif char in "\"'{}()_-,.!":
      score += 1
  return score
