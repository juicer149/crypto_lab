from ciphers.cipher_base import CipherBase


class ScytalCipher(CipherBase):
    def encrypt(self) -> str:
        result = []
        for col in range(self.columns):
            for row in range(self.rows):
                index = row * self.columns + col
                result.append(self.padded_text[index])
        return ''.join(result)

    def decrypt(self) -> str:
        result = [''] * (self.rows * self.columns)
        index = 0
        for col in range(self.columns):
            for row in range(self.rows):
                pos = row * self.columns + col
                if pos < len(self.clean_text):  # undvik att fylla padding
                    result[pos] = self.original_text[index]
                    index += 1
        return ''.join(result).strip()

