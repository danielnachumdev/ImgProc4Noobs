from abc import ABC, abstractmethod
import numpy as np


class QuantizationStrategy(ABC):
    @staticmethod
    @abstractmethod
    def quantize(arr: np.ndarray, k: int, minimal_value: float = 0, maximal_value: float = 255) -> np.ndarray:
        pass
