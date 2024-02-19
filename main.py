from src import *


class Dummy(Serializable):
    def __init__(self, s: str):
        self.s = s

    @staticmethod
    def deserialize(serialized: SerializationStr) -> "Serializable":
        return Dummy(serialized)

    def serialize(self) -> SerializationStr:
        return self.s

    def __str__(self):
        return f"{self.__class__.__qualname__}(s={self.s})"


def main() -> None:
    print(Dummy.deserialize(LZW.decode(LZW.encode(Dummy("babaabaaa")))))
    print()

if __name__ == "__main__":
    main()
