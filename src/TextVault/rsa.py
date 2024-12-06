import random
from math import gcd
from base_class import Encryptor

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

# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:  # Ensure p and q are different
        q = generate_prime()

    n = p * q  # for public and private key
    phi = (p - 1) * (q - 1) #Euler's Totient Function: phi(n)=(p−1)×(q−1)

    # Choose public exponent e
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1]) # for public key

    # Compute private key d
    d = modular_inverse(e, phi) # for private key

    return (e, n), (d, n)  # Public key, Private key

# Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    block_size = len(base36_encode(n))  # Calculate the maximum block size for Base36
    cipher = [
        base36_encode((ord(char) ** e) % n).zfill(block_size)  # Pad with zeros
        for char in plaintext
    ]
    return ''.join(cipher)  # Combine blocks into a single string

# Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    block_size = len(base36_encode(n))  # Use the same block size as encryption
    # Split the ciphertext into fixed-size blocks
    blocks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]
    plain = ''.join([chr((base36_decode(block) ** d) % n) for block in blocks])
    return plain

# Function to save keys to text files
def save_keys(public_key, private_key):
    with open("public_key.txt", "w") as pub_file:
        pub_file.write(f"{public_key[0]}\n{public_key[1]}")
    with open("private_key.txt", "w") as priv_file:
        priv_file.write(f"{private_key[0]}\n{private_key[1]}")

# Function to load keys from text files
def load_key(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        return int(lines[0].strip()), int(lines[1].strip())
