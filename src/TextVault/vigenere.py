try: from .base_class import Encryptor, Key
except ImportError: from base_class import Encryptor, Key

class VigenereEncryptor(Encryptor):
    """
    A class that implements Vigenère cipher encryption and decryption using a symmetric key.
    """

    def newkey(self) -> tuple[int, int]:
        """
        Generates a new random symmetric key for the Vigenère cipher.

        Returns:
            tuple[int, int]: A tuple representing a symmetric key.
        """
        import random
        import string

        key_length = 10  # Set the length of the key
        key = tuple(random.choice(string.ascii_uppercase) for _ in range(key_length))

        return key

    def encrypt(self, text: str, key: tuple[int, int]) -> str:
        """
        Encrypts a given text using the provided Vigenère key.

        Args:
            text (str): The plaintext message to be encrypted.
            key (tuple[int, int]): A tuple representing the symmetric key.

        Returns:
            str: The encrypted message.
        """
        key_value = ''.join(key)  # Convert tuple to string
        encrypted_text = []
        key_length = len(key_value)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key_value[i % key_length]) - ord('A')
                if char.islower():
                    encrypted_text.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
                else:
                    encrypted_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                encrypted_text.append(char)  # Keep non-alphabet characters as is

        return ''.join(encrypted_text)

    def decrypt(self, text: str, key: tuple[int, int]) -> str:
        """
        Decrypts an encrypted text back to its original form using the provided key.

        Args:
            text (str): The encrypted message to be decrypted.
            key (tuple[int, int]): A tuple representing the symmetric key.

        Returns:
            str: The original plaintext message.
        """
        key_value = ''.join(key)  # Convert tuple to string
        decrypted_text = []
        key_length = len(key_value)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key_value[i % key_length]) - ord('A')
                if char.islower():
                    decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                else:
                    decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                decrypted_text.append(char)  # Keep non-alphabet characters as is

        return ''.join(decrypted_text)

"""
enc = VigenereEncryptor()

key = enc.newkey()
a = enc.encrypt("Hello, World!", key)

print(a)
A = enc.decrypt(a, key)
print(A)

"""
