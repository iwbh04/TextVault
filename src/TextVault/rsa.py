import random
from math import gcd

# Function to generate a large prime number
def generate_prime():
    while True:
        num = random.randint(100, 999)  # Generate a 3-digit number (for simplicity to shorten run time)
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

# Function to find modular inverse--> formula: (e x d) mod phi(n) = 1
def modular_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1: 
            return d
    return None

# Base36 Encoding
def base36_encode(num):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    result = []
    while num:
        num, rem = divmod(num, 36)
        result.append(chars[rem])
    return ''.join(reversed(result))

# Base36 Decoding
def base36_decode(encoded_str):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = 0
    for char in encoded_str:
        num = num * 36 + chars.index(char)
    return num



