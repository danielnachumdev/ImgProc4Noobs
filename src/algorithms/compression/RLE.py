from typing import Generator

from src import Serializable, Code, SerializationStr
from .compression_algorithm import CompressionAlgorithm


class RLE(CompressionAlgorithm):
    """
    Run Length Encoding
    """

    @staticmethod
    def decode(generator: Generator[Code, None, None]) -> SerializationStr:
        res = ""
        for c, amount in generator:
            res += c * amount
        return res

    @staticmethod
    def encode(obj: Serializable) -> Generator[Code, None, None]:
        s = obj.serialize()
        i = 0
        while i < len(s):
            j = 1
            while s[i + j] == s[i]:
                j += 1
            j -= 1
            yield (s[i], j)
            i += 1


__all__ = [
    "RLE"
]
