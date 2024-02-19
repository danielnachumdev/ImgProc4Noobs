from typing import Generator

from interfaces.serializable import Serializable, SerializationStr
from interfaces.compression_strategy import CompressionStrategy, Code


class PyramidCompression(CompressionStrategy):
    @staticmethod
    def decode(g: Generator[Code, None, None]) -> SerializationStr:
        pass

    @staticmethod
    def encode(obj: Serializable) -> Generator[Code, None, None]:
        pass


__all__ = [
    "PyramidCompression"
]
