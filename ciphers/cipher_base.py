from abc import ABC, abstractmethod
import math


class CipherBase(ABC):
    def __init__(self, text: str, columns: int):
        self.original_text = text
        self.columns = columns
        self.clean_text = self._normalize(text)
        self.rows = math.ceil(len(self.clean_text) / self.columns)
        self.padded_text = self._pad(self.clean_text)

    def _normalize(self, text: str) -> str:
        return text.replace(" ", "").upper()

    def _pad(self, text: str) -> str:
        target_length = self.rows * self.columns
        return text.ljust(target_length)

    @abstractmethod
    def encrypt(self) -> str:
        pass

    @abstractmethod
    def decrypt(self) -> str:
        pass
