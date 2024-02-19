from abc import ABC, abstractmethod
from typing import Generator, TypeVar
from interfaces.serializable import Serializable, SerializationStr

Code = TypeVar("Code")


class CompressionStrategy(ABC):

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
    "CompressionStrategy",
]
