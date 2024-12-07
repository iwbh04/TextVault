from base_class import *
import random
import numpy as np

class HillCipherWithNumbers(Encryptor):
    """
    A modified Hill Cipher class that processes strings containing alphabets and numbers.
    Implements encryption and decryption by separating characters into ASCII codes (for alphabets) and numbers.
    Automatically generates a random key matrix for encryption.
    """

    def __init__(self, size=2):
        self.size = size
        self.key_matrix = self._generate_key_matrix(size)
        self.mod = 128  # Using ASCII range

    def _generate_key_matrix(self, size):
        while True:
            matrix = [[random.randint(0, self.mod - 1) for _ in range(size)] for _ in range(size)]
            try:
                # Ensure the matrix is invertible
                np.linalg.inv(np.array(matrix))
                return np.array(matrix)
            except np.linalg.LinAlgError:
                continue  # Retry if the matrix is not invertible

    def _char_to_num(self, char):
        if char.isalpha():
            return ord(char)  # Use ASCII code for alphabets
        elif char.isdigit():
            return int(char)  # Keep numbers as integers

    def _num_to_char(self, num):
        if 0 <= num < 128:
            return chr(num)  # Convert ASCII back to character
        else:
            raise ValueError("Invalid number for conversion to character")

    def _process_text(self, text):
        nums = [self._char_to_num(char) for char in text]
        while len(nums) % self.size != 0:
            nums.append(0)  # Padding with 0
        return np.array(nums)

    def encrypt(self, plaintext):
        nums = self._process_text(plaintext)
        nums = nums.reshape(-1, self.size)
        encrypted_nums = (np.dot(nums, self.key_matrix) % self.mod).flatten()
        return encrypted_nums.tolist()

    def decrypt(self, encrypted_nums):
        encrypted_nums = np.array(encrypted_nums)
        encrypted_nums = encrypted_nums.reshape(-1, self.size)
        inverse_key = np.linalg.inv(self.key_matrix) % self.mod
        inverse_key = np.round(inverse_key).astype(int)  # Ensure integers
        decrypted_nums = (np.dot(encrypted_nums, inverse_key) % self.mod).flatten()
        return ''.join(self._num_to_char(int(round(num))) for num in decrypted_nums if num != 0)

# Example usage
if __name__ == "__main__":
    cipher = HillCipherWithNumbers(size=2)

    plaintext = "A1B2C3"
    print("Original Text:", plaintext)

    print("Generated Key Matrix:")
    print(cipher.key_matrix)

    encrypted = cipher.encrypt(plaintext)
    print("Encrypted Text (as numbers):", encrypted)

    decrypted = cipher.decrypt(encrypted)
    print("Decrypted Text:", decrypted)

    # Verification
    if plaintext == decrypted:
        print("Success: Decrypted text matches the original!")
    else:
        print("Error: Decrypted text does not match the original.")
