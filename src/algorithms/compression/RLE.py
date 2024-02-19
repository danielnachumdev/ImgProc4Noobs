from typing import Generator

from interfaces.serializable import Serializable, SerializationStr
from interfaces.compression_strategy import CompressionStrategy, Code


class RLE(CompressionStrategy):
    """
    Run Length Encoding
    """

    @staticmethod
    def decode(g: Generator[Code, None, None]) -> SerializationStr:
        res = ""
        for c, amount in g:
            res += c * amount
        return res

    @staticmethod
    def encode(obj: Serializable) -> Generator[Code, None, None]:
        s = obj.serialize()
        i = 0
        while i < len(s):
            j = 1
            while i + j < len(s) and s[i + j] == s[i]:
                j += 1
            yield (s[i], j)
            i += j


__all__ = [
    "RLE"
]
