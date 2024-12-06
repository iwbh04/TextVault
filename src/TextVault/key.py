import random
from math import gcd
from base import Encryptor

def generate_prime():
    """Generate a random 3-digit prime number."""
    while True:
        num = random.randint(100, 999)
        if is_prime(num):
            return num

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def modular_inverse(e, phi):
    """Find the modular inverse of e modulo phi."""
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys():
    """Generate RSA public and private keys."""
    p = generate_prime()
    q = generate_prime()
    while q == p:  # Ensure p and q are different
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    d = modular_inverse(e, phi)

    return (e, n), (d, n)  # Public key, Private key

class Key:
    def __init__(self, value: str, encryptor: 'Encryptor'):
        """
        Represents a cryptographic key.

        Args:
            value (str): The key's value, typically formatted as a string.
            encryptor (Encryptor): The encryptor instance that manages this key.
        """
        self.value = value
        self.encryptor = encryptor

    def __repr__(self):
        return f"Key(value='{self.value}')"
