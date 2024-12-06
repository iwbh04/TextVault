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

