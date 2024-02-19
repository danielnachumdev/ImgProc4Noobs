from typing import Generator

from utils.serializable import Serializable, SerializationStr
from .compression_algorithm import CompressionAlgorithm, Code


class LZW(CompressionAlgorithm):
    """
    Lempel-Ziv compression algorithm
    """

    @staticmethod
    def decode(g: Generator[Code, None, None]) -> SerializationStr:
        highest_value = 255
        d = {c: chr(c) for c in range(highest_value)}
        O = next(g)
        res = d[O]
        for N in g:
            if N not in d:
                S = d[O]
                S = S + C
            else:
                S = d[N]
            res += S
            C = S[0]
            highest_value += 1
            d[d[O] + C] = highest_value
            O = N
        return res

    @staticmethod
    def encode(obj: Serializable) -> Generator[Code, None, None]:
        highest_value = 255
        t: str = obj.serialize()
        P = t[0]
        i = 0
        d = {chr(c): c for c in range(highest_value)}
        while i < len(t):
            C = t[i + 1]
            if P + C in d:
                P = P + C
            else:
                yield d[P]
                highest_value += 1
                d[P + C] = highest_value
                P = C
            i += 1

        yield d[P]


__all__ = [
    "LZW"
]
