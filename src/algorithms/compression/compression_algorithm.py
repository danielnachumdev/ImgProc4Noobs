from abc import ABC, abstractmethod
from typing import Generator, TypeVar
from src.utils.serializable import Serializable, SerializationStr

Code = TypeVar("Code")


class CompressionAlgorithm(ABC):

    @staticmethod
    @abstractmethod
    def encode(obj: Serializable) -> Generator[Code, None, None]:
        pass

    @staticmethod
    @abstractmethod
    def decode(generator: Generator[Code, None, None]) -> SerializationStr:
        pass


__all__ = [
    "Code",
    "CompressionAlgorithm"
]
