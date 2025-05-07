import unittest
from cryptolib.encrypt import Caesar, Vigenere
from cryptolib.decrypt import Caesar as CaesarDecrypt, Vigenere as VigenereDecrypt

class TestEncryptionAlgorithms(unittest.TestCase):
    def test_caesar_encryption(self):
        result = Caesar("hello world", 3)
        self.assertEqual(result, "khoor zruog")
    
    def test_caesar_decryption(self):
        result = CaesarDecrypt("khoor zruog", 3)
        self.assertEqual(result, "hello world")

    def test_vigenere_encryption(self):
        result = Vigenere("hello world", "key")
        self.assertEqual(result, "ripxe sjbiu")
    
    def test_vigenere_decryption(self):
        result = VigenereDecrypt("ripxe sjbiu", "key")
        self.assertEqual(result, "hello world")

if __name__ == '__main__':
    unittest.main()
