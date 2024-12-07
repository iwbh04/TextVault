Usage
=====

Installation
------------

To use TextVault, first install it using pip:

.. code-block:: console

    (.venv) $ pip install TextVault

Knapsack Encryptor
==================
.. autoclass:: TextVault.KnapsackEncryptor
    :members:
    :member-order: bysource
.. autoclass:: TextVault.KnapsackKey
    :members:
    :member-order: bysource

RSA Encryption Module
=====================

This module implements the RSA encryption and decryption algorithm, providing functionality for key generation, encryption, decryption, and saving/loading keys to/from text files.

Overview
--------

The RSA algorithm is an asymmetric cryptographic system that uses a pair of keys:
- **Public Key**: Used to encrypt messages.
- **Private Key**: Used to decrypt messages.

This implementation includes support for Base36 encoding, which allows encrypted messages to be represented as a mix of letters and numbers.

Features
--------
- Generate RSA public and private keys.
- Encrypt plaintext messages using a public key.
- Decrypt ciphertext messages using a private key.
- Save and load keys to and from text files.
- Supports Base36 encoding for ciphertext representation.

Installation
------------

To use this module, clone the repository and import the required functions directly into your project.

Requirements:
- Python 3.7 or higher.
- Standard libraries: `math`, `random`.

Usage
-----

### Key Generation

The `generate_keys()` function generates a pair of RSA keys (public and private). The keys consist of the following components:
- **Public Key**: `(e, n)`
- **Private Key**: `(d, n)`

Example:

```python
from rsa import generate_keys

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)


Vigenère Encryption Module
==========================

This module implements the Vigenère cipher algorithm, providing functionality to encrypt and decrypt given text using a secret key.

Core Concept
-------------
The Vigenère cipher is a symmetric encryption technique, meaning the same key is used for both encryption and decryption. The key is a string of alphabetic characters, and each character in the text is shifted based on the position of the corresponding character in the key.

How It Works
------------
- The `newkey()` method generates a random encryption key.
- The `encrypt()` method encrypts plaintext text using the provided key to produce a ciphertext.
- The `decrypt()` method decrypts the ciphertext back into the original plaintext using the same key.

Features
--------
- Randomly generates a Vigenère encryption key.
- Encrypts and decrypts text using the same key.
- Differentiates between uppercase and lowercase letters, while leaving non-alphabetic characters unchanged.

Installation and Requirements
-----------------------------
To use this module, simply import the necessary classes into your project.

Requirements:
- Python 3.7 or higher
- Standard libraries: random, string

Working Principle
-----------------
The Vigenère cipher is based on a repeated Caesar cipher technique. For each character in the text, the corresponding character in the key determines the shift applied to that letter. For example, an "A" would be shifted by the value of the key character "K", and a "B" would be shifted by the value of the next character in the key.

Usage Example
--------------
Here’s an example of how to use the Vigenère encryption module:

```python
from vigenere import VigenereEncryptor

# Create an instance of the Vigenère encryption object
encryptor = VigenereEncryptor()

# Generate a new key
public_key, private_key = encryptor.newkey()

# Print the generated key
print("Generated Key (Public & Private):", public_key.value)

# Example of encrypting text
text = "Hello World!"
encrypted = encryptor.encrypt(text, public_key)
print("Encrypted Text:", encrypted)

# Example of decrypting the text
decrypted = encryptor.decrypt(encrypted, private_key)
print("Decrypted Text:", decrypted)
