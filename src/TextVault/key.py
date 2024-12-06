import random
from math import gcd
import random

# Function to generate a large prime number
def generate_prime():
    while True:
        num = random.randint(100, 999)  # Generate a 3-digit number (for simplicity)
        if is_prime(num):
            return num

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find modular inverse
def modular_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:  # Ensure p and q are different
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent e
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])

    # Compute private key d
    d = modular_inverse(e, phi)

    return (e, n), (d, n)  # Public key, Private key
