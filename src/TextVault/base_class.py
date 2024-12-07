from abc import ABC, abstractmethod
from typing import Any

class Key:
    def __init__(self, value):
        self.value: Any = value

class Encryptor(ABC):
    @abstractmethod
    def newkey(self) -> Key | tuple[Key]:
        pass
    
    @abstractmethod
    def encrypt(self, text: str, key: Key) -> str:
        pass
    
    @abstractmethod
    def decrypt(self, text: str, key: Key) -> str:
        pass

# class LengthLimitExceed(Exception):
#     # 암호화 가능한 문자열의 길이를 초과한 경우
#     pass

# class KeyTypeNotMatch(Exception):
#     pass