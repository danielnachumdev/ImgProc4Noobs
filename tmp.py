from src import *



def main() -> None:
    print(RLE.decode(RLE.encode(DummySerializable("babaabaaa"))))
    # print(LZW.decode(LZW.encode(Dummy("babaabaaa"))))


if __name__ == "__main__":
    main()
