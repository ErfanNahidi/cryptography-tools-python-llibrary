import string
from .core import normalize_text

def Caesar(plain_text, key):
    alphabet = string.ascii_lowercase
    plain_text = normalize_text(plain_text)
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            new_index = (alphabet.index(char) - key) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    return cipher_text

def Vigenere(plain_text, key):
    alphabet = string.ascii_lowercase
    plain_text = normalize_text(plain_text)
    key = normalize_text(key)
    cipher_text = ''
    key_index = 0
    for char in plain_text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            new_index = (alphabet.index(char) - shift) % len(alphabet)
            cipher_text += alphabet[new_index]
            key_index = (key_index + 1) % len(key)
        else:
            cipher_text += char
    return cipher_text
