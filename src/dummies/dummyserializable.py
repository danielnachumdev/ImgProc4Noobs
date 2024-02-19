from interfaces.serializable import Serializable, SerializationStr


class DummySerializable(Serializable):
    def __init__(self, s: str):
        self.s = s

    @staticmethod
    def deserialize(serialized: SerializationStr) -> "Serializable":
        return DummySerializable(serialized)

    def serialize(self) -> SerializationStr:
        return self.s

    def __str__(self):
        return f"{self.__class__.__qualname__}(s={self.s})"

    def __eq__(self, other: "DummySerializable") -> bool:
        return self.s == other.s


__all__ = [
    "DummySerializable"
]
