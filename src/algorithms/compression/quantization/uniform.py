import numpy as np

from interfaces.quantization_strategy import QuantizationStrategy


class UniformQuantization(QuantizationStrategy):
    @staticmethod
    def quantize(arr: np.ndarray, k: int, minimal_value: float = 0.0, maximal_value: float = 255.0) -> np.ndarray:
        hist, bins = np.histogram(arr, bins=k, range=(minimal_value, maximal_value))
        pass
