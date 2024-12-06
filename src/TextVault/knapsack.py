from base_class import *
import random
import base64

class KnapsackEncryptor(Encryptor):
    # 설명 작성 필요

    @staticmethod
    def __encode(li: list[int]) -> str:
        b = b','.join(base64.b64encode(i.to_bytes(16)) for i in li)
        return b.decode()

    @staticmethod
    def __decode(txt: str) -> list[int]:
        ret = [int.from_bytes(base64.b64decode(i)) for i in txt.split(',')]
        return ret
    
    def encrypt(self, text: str, key: Key) -> str:
        if key.encryptor != self.__class__: raise KeyTypeNotMatch("Encryptor doesn't match")
        key = self.__decode(key.value)

        # 임시로 각 값의 ord를 사용
        binary_message = [f'{ord(c):0{len(key)}b}' for c in text]

        encrypted = [sum(int(x[i])*key[i] for i in range(len(key))) for x in binary_message]
        return self.__encode(encrypted)
    
    def decrypt(self, text: str, key: Key) -> str:
        if key.encryptor != self.__class__: raise KeyTypeNotMatch("Encryptor doesn't match")
        key = self.__decode(key.value)
        if len(key) < 3: raise KeyTypeNotMatch("Key format doesn't match")

        *arr, mod, mult = key
        inv_mult = pow(mult, -1, mod)
        
        encrypted = self.__decode(text)
        encrypted = [i*inv_mult%mod for i in encrypted]

        recovered = []
        for sum_val in encrypted:
            cur = []
            for value in reversed(arr):
                if sum_val >= value:
                    cur.append('1')
                    sum_val -= value
                else:
                    cur.append('0')
            recovered.append(int(''.join(cur)[::-1],2))

        return ''.join(chr(i) for i in recovered)
    
    def newkey(self) -> Key | tuple[Key]:
        length = 10

        def isprime(n):
            if n<=1: return False
            for i in range(2, int(n**.5)+1):
                if n%i == 0: break
            else: return True
            return False

        # 초증가 수열 (이전 수들의 합보다 다음 수의 값이 큼)
        private_key = []
        sm = 0
        for _ in range(length):
            private_key.append(sm + random.randint(1,50))
            sm += private_key[-1]
        
        while 1:
            mod = random.randint(sm+1, 65536)
            if isprime(mod): break
        
        mult = random.randint(10,mod-1)

        # private_key = [2, 4, 6, 13, 27, 55, 111]
        # mod = 211
        # mult = 17

        public_key = [(x * mult) % mod for x in private_key]
        private_key += [mod, mult]

        return Key(self.__encode(public_key), self.__class__), Key(self.__encode(private_key), self.__class__)

"""
enc = KnapsackEncryptor()

pub, priv = enc.newkey()
a = enc.encrypt("Hello, World!", pub)

print(a)
A= enc.decrypt(a, priv)
print(A)
"""