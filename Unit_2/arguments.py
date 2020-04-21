import sys

phrase = sys.argv[1]
shift = int(sys.argv[2])

def shift_letter(letter, shift):
    index = alphabet.index(letter)
    index = (index + shift) % 26
    return alphabet[index]

def cæsar_shift(phrase, shift):
    result = ''
    for letter in phrase:
        result += shift_letter(letter, shift)
    return result

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(cæsar_shift(phrase, shift))