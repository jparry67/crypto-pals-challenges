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
