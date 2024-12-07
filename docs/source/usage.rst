Usage
=====

Installation
------------

To use TextVault, first install it using pip:

.. code-block:: console

    (.venv) $ pip install TextVault

Knapsack Encryption Module
==================
Overview
--------
This module includes Knapsack Encryptor and Key class.
Encryptor class implements `Merkle-Hellman knapsack cryptosystem<https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem>`.


API Reference
-------------
.. autoclass:: TextVault.KnapsackEncryptor
    :members:
    :member-order: bysource
.. autoclass:: TextVault.KnapsackKey
    :members:
    :member-order: bysource

Example
-------
.. code-block:: python
    
    # After `$ pip install TextVault`

    from TextVault import KnapsackEncryptor
    txt = "Hello, World!"
    enc = KnapsackEncryptor()

    pub, priv = enc.newkey()
    encrypted = enc.encrypt(txt, pub)
    decrypted = enc.decrypt(a, priv)

    print("Public key:", pub)
    print("Private key:", priv)

    print("Original:", txt)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

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

.. code-block:: python

    from rsa import generate_keys

    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)


Vigenère Encryption Module
==========================

This module implements the Vigenère cipher algorithm, providing functionality to encrypt and decrypt text using a symmetric key.

Core Concept
-------------
The Vigenère cipher is a symmetric encryption technique, meaning the same key is used for both encryption and decryption. The key is a string of uppercase alphabetic characters, and each character in the text is shifted based on the position of the corresponding character in the key.

How It Works
------------
- The `newkey()` method generates a random encryption key of fixed length (10 characters in this case).
- The `encrypt()` method takes plaintext and encrypts it using the provided key.
- The `decrypt()` method decrypts the encrypted text back to its original form using the same key.

Features
--------
- Randomly generates a symmetric Vigenère encryption key.
- Encrypts and decrypts text with the same key.
- Supports both uppercase and lowercase letters, while non-alphabetic characters remain unchanged.

Installation and Requirements
-----------------------------
To use this module, simply import the necessary classes into your project.

Requirements:
- Python 3.7 or higher
- Standard libraries: random, string

Working Principle
-----------------
The Vigenère cipher uses a key of repeated characters to shift each character in the text. The shift value for each character is determined by the corresponding character in the key. For example, if the key character is "A", the text character is unchanged, but if the key character is "B", the text character is shifted by one position in the alphabet.

Usage Example
--------------
Here’s an example of how to use the Vigenère encryption module:

.. code-block:: python

    from vigenere import VigenereEncryptor

    # Create an instance of the Vigenère encryption object
    encryptor = VigenereEncryptor()

    # Generate a new key
    key = encryptor.newkey()

    # Print the generated key
    print("Generated Key:", key.value)

    # Example of encrypting text
    text = "Hello World!"
    encrypted = encryptor.encrypt(text, key)
    print("Encrypted Text:", encrypted)

    # Example of decrypting the text
    decrypted = encryptor.decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)
