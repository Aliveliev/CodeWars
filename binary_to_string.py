'''
    Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

    Each 8 bits on the binary string represent 1 character on the ASCII table.

    The input string will always be a valid binary string.

    Characters can be in the range from "00000000" to "11111111" (inclusive)

    Note: In the case of an empty binary string your function should return an empty strin
'''

def binary_to_string(binary: str) -> str:
    return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])

assert binary_to_string('0100100001100101011011000110110001101111') == 'Hello'
assert binary_to_string('00110001001100000011000100110001') == '1011'

def string_to_binary(string: str) -> str:
    return ''.join([f'{(ord(ch)):08b}' for ch in string])

assert string_to_binary('Hello') == '0100100001100101011011000110110001101111'
assert string_to_binary('1011') == '00110001001100000011000100110001'

print(string_to_binary('Hello, my name is Ali'))