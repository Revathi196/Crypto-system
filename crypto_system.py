from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class CryptoSystem:
    def __init__(self, key=None):
        """Initialize the CryptoSystem. If no key is provided, generate a random one."""
        self.block_size = AES.block_size
        if key:
            self.key = key
        else:
            self.key = get_random_bytes(16)  # 128-bit key

    def encrypt(self, plaintext):
        """Encrypt a message using AES encryption with CBC mode."""
        cipher = AES.new(self.key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext.encode(), self.block_size))
        # Base64 encode the IV and ciphertext to store them together as a string
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        encrypted_msg = base64.b64encode(ciphertext).decode('utf-8')
        return iv, encrypted_msg

    def decrypt(self, iv, ciphertext):
        """Decrypt a message using AES encryption with CBC mode."""
        iv = base64.b64decode(iv)
        ciphertext = base64.b64decode(ciphertext)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), self.block_size)
        return decrypted_data.decode()

    def save_key(self, filename):
        """Save the encryption key to a file."""
        with open(filename, 'wb') as file:
            file.write(self.key)

    def load_key(self, filename):
        """Load the encryption key from a file."""
        with open(filename, 'rb') as file:
            self.key = file.read()

    def get_key(self):
        """Return the current encryption key (for testing purposes)."""
        return self.key
