from abc import ABC, abstractmethod
from typing import TypeVar

SerializationStr = TypeVar('SerializationStr', bound=str)


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> SerializationStr:
        pass

    @staticmethod
    @abstractmethod
    def deserialize(serialized: SerializationStr) -> "Serializable":
        pass


__all__ = [
    "SerializationStr",
    "Serializable"
]
