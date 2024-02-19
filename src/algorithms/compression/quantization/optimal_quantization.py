import numpy as np

from interfaces.quantization_strategy import QuantizationStrategy


class OptimalQuantization(QuantizationStrategy):
    @staticmethod
    def quantize(arr: np.ndarray, k: int, minimal_value: float = 0, maximal_value: float = 255) -> np.ndarray:
        pass
