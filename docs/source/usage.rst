Usage
=====



Installation
------------

To use TEXTVAULT_LIBRARY, first install it using pip:

.. code-block:: console

    (.venv) $ pip install TEXTVAULT_LIBRARY

RSA Encryption Module
=====================

This module implements the RSA encryption and decryption algorithm, along with utilities for key generation, encryption, decryption, and saving/loading keys. It includes Base36 encoding for handling mixed numeric and alphabetic ciphertext.

Overview
--------

RSA (Rivest–Shamir–Adleman) is an asymmetric cryptographic algorithm that uses two keys:
- **Public Key (e, n):** Used to encrypt messages.
- **Private Key (d, n):** Used to decrypt messages.

This module provides functions for:
- Generating RSA keys.
- Encrypting plaintext into ciphertext.
- Decrypting ciphertext back into plaintext.
- Saving and loading keys from text files.

Functions
---------

### `generate_prime()`
Generate a random 3-digit prime number.

**Returns:**
    - `int`: A randomly chosen prime number.

### `is_prime(n)`
Check if a number is prime.

**Parameters:**
    - `n (int)`: The number to check.

**Returns:**
    - `bool`: `True` if `n` is prime, otherwise `False`.

### `modular_inverse(e, phi)`
Find the modular multiplicative inverse of `e` modulo `phi`.

**Parameters:**
    - `e (int)`: The public exponent.
    - `phi (int)`: Euler's Totient function value.

**Returns:**
    - `int`: The modular inverse `d`, such that `(e * d) % phi == 1`.

### `base36_encode(num)`
Encode an integer into a Base36 string (0-9, A-Z).

**Parameters:**
    - `num (int)`: The integer to encode.

**Returns:**
    - `str`: The Base36-encoded string.

### `base36_decode(encoded_str)`
Decode a Base36 string back into an integer.

**Parameters:**
    - `encoded_str (str)`: The Base36 string to decode.

**Returns:**
    - `int`: The decoded integer.

### `generate_keys()`
Generate RSA public and private keys.

**Returns:**
    - `tuple`: A tuple containing:
        - `(e, n)`: The public key.
        - `(d, n)`: The private key.

### `encrypt(public_key, plaintext)`
Encrypt a plaintext string using the RSA public key.

**Parameters:**
    - `public_key (tuple)`: The public key `(e, n)`.
    - `plaintext (str)`: The plaintext message.

**Returns:**
    - `str`: The encrypted message as a Base36-encoded string.

### `decrypt(private_key, ciphertext)`
Decrypt a ciphertext string using the RSA private key.

**Parameters:**
    - `private_key (tuple)`: The private key `(d, n)`.
    - `ciphertext (str)`: The encrypted Base36-encoded message.

**Returns:**
    - `str`: The original plaintext message.

### `save_keys(public_key, private_key)`
Save the RSA public and private keys to text files.

**Parameters:**
    - `public_key (tuple)`: The public key `(e, n)`.
    - `private_key (tuple)`: The private key `(d, n)`.

**Output Files:**
    - `public_key.txt`: Stores the public key.
    - `private_key.txt`: Stores the private key.

### `load_key(file_path)`
Load a key from a text file.

**Parameters:**
    - `file_path (str)`: The path to the key file.

**Returns:**
    - `tuple`: A tuple containing the key components `(value1, value2)`.

Usage
-----

### Example: Key Generation
Generate RSA public and private keys:
```python
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)
