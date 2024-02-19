import numpy as np


class Image:
    @staticmethod
    def black():
        pass

    def __init__(self, np_arr):
        self.arr = np_arr


__all__ = [
    "Image"
]
