from rsa import generate_prime, modular_inverse,base36_encode,base36_decode
from math import gcd
import random

class Key:
    def __init__(self, value, encryptor):
        self.value: str = value
        self.encryptor: Encryptor = encryptor
    
    def export(self, file_name: str):
        with open(file_name, "r") as file:
            lines = file.readlines()
            return int(lines[0].strip()), int(lines[1].strip())

class Encryptor():
    def newkey() -> Key | tuple[Key]:
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

    def encrypt(public_key, plaintext):
        e, n = public_key
        block_size = len(base36_encode(n))  # Calculate the maximum block size for Base36
        cipher = [
            base36_encode((ord(char) ** e) % n).zfill(block_size)  # Pad with zeros
            for char in plaintext
        ]
        return ''.join(cipher)  # Combine blocks into a single string
    
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

# class LengthLimitExceed(Exception):
#     # 암호화 가능한 문자열의 길이를 초과한 경우
#     pass

# class KeyTypeNotMatch(Exception):
#     pass
