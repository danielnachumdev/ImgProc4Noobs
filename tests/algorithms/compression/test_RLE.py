import unittest
from src import RLE, DummySerializable


class TestRLE(unittest.TestCase):
    def test_RLE(self):
        s = "babaabaaa"
        self.assertEqual(s, RLE.decode(RLE.encode(DummySerializable(s))))
