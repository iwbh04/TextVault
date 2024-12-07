from base_class import Key, Encryptor

class VigenereEncryptor(Encryptor):
    
    def newkey(self):
    
        import random
        import string
        
        key_length = 10  # Set the length of the key
        key = ''.join(random.choice(string.ascii_uppercase) for _ in range(key_length))
        pub = Key(value=key, encryptor=self)
        priv = Key(value=key, encryptor=self)  # For Vigenère, both keys are the same
        return pub, priv

    def encrypt(self, text: str, key: Key) -> str:
        
        key_value = key.value
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

    def decrypt(self, text: str, key: Key) -> str:
        
        key_value = key.value
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

pub,priv = enc.newkey()
a = enc.encrypt("Hello, World!", pub)

print(a)
A= enc.decrypt(a, priv)
print(A)

"""
