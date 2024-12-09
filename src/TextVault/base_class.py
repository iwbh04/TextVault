from abc import ABC, abstractmethod
from typing import Any

class Key:
    def __init__(self, value):
        self.value: Any = value
    
    def __repr__(self):
        '''return ``f"Key({self.value})"``'''
        return f"Key({self.value})"
    
    def __str__(self):
        return self.__repr__()

class Encryptor(ABC):
    @abstractmethod
    def newkey(self) -> Key | tuple[Key, Key]:
        pass
    
    @abstractmethod
    def encrypt(self, text: str, key: Key) -> str:
        pass
    
    @abstractmethod
    def decrypt(self, text: str, key: Key) -> str:
        pass
