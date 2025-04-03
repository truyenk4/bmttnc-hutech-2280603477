from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class RSACipher:
    def __init__(self):
        self.key = None
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.private_key = self.key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(message.encode())

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(ciphertext).decode()

    def sign(self, message, private_key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

    def load_keys(self):
        return self.private_key, self.public_key