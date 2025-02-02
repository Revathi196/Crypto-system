# Cryptography System

This is a simple command-line cryptography system that provides encryption and decryption functionalities using **AES (Advanced Encryption Standard)** with **CBC (Cipher Block Chaining) mode**. The system allows users to encrypt and decrypt messages securely, manage encryption keys, and store them for later use.

## Features

- **Encrypt a Message**: Encrypt messages using AES with CBC mode and a randomly generated or pre-loaded encryption key.
- **Decrypt a Message**: Decrypt messages that were previously encrypted using the system.
- **Save Encryption Key**: Save the encryption key to a file for future use.
- **Load Encryption Key**: Load the encryption key from a file to continue encrypting and decrypting messages.

## Files in the Repository

### 1. `crypto_system.py`

This file contains the core cryptographic functions used in the system:

- **`CryptoSystem` class**: Handles encryption, decryption, key management, and other cryptographic operations.
  - **`encrypt()`**: Encrypts a plaintext message using AES and returns the encrypted message and initialization vector (IV).
  - **`decrypt()`**: Decrypts an encrypted message using the AES key and IV.
  - **`save_key(filename)`**: Saves the current encryption key to a specified file.
  - **`load_key(filename)`**: Loads the encryption key from a specified file.
  - **`get_key()`**: Returns the current encryption key (for debugging
