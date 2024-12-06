from base_class import Key, Encryptor

class RSAEncryptor(Encryptor):
    def newkey(self) -> tuple[Key, Key]:
        public_key, private_key = generate_keys()
        pub_key_obj = Key(value=f"{public_key[0]}:{public_key[1]}", encryptor=self)
        priv_key_obj = Key(value=f"{private_key[0]}:{private_key[1]}", encryptor=self)
        return pub_key_obj, priv_key_obj

    def encrypt(self, text: str, key: Key) -> str:
        e, n = map(int, key.value.split(':'))
        encrypted = [pow(ord(char), e, n) for char in text]
        return ' '.join(map(str, encrypted))

    def decrypt(self, text: str, key: Key) -> str:
        d, n = map(int, key.value.split(':'))
        encrypted_numbers = map(int, text.split())
        decrypted = ''.join(chr(pow(num, d, n)) for num in encrypted_numbers)
        return decrypted
