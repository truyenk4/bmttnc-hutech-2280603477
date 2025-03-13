class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A')))