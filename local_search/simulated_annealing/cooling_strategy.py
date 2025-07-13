from abc import ABC, abstractmethod
import math


class CoolingStrategy(ABC):
    """Abstract base class for cooling strategies"""

    @abstractmethod
    def cool(self, current_temperature: float, step: int, **kwargs) -> float:
        """Calculate new temperature based on current temperature and step"""
        pass


class ExponentialCooling(CoolingStrategy):
    """Exponential cooling: T = T * cooling_rate"""

    def __init__(self, cooling_rate: float = 0.95):
        self.cooling_rate = cooling_rate

    def cool(self, current_temperature: float, step: int, **kwargs) -> float:
        return current_temperature * self.cooling_rate


class LinearCooling(CoolingStrategy):
    """Linear cooling: T = T - cooling_rate"""

    def __init__(self, cooling_rate: float = 1.0):
        self.cooling_rate = cooling_rate

    def cool(self, current_temperature: float, step: int, **kwargs) -> float:
        return max(0, current_temperature - self.cooling_rate)


class LogarithmicCooling(CoolingStrategy):
    """Logarithmic cooling: T = c / log(step + 1)"""

    def __init__(self, c: float = 100):
        self.c = c

    def cool(self, current_temperature: float, step: int, **kwargs) -> float:
        return self.c / math.log(step + 2)


class InverseCooling(CoolingStrategy):
    """Inverse cooling: T = initial_T / (1 + alpha * step)"""

    def __init__(self, alpha: float = 0.01):
        self.alpha = alpha

    def cool(
        self,
        current_temperature: float,
        step: int,
        initial_temperature: float = None,
        **kwargs,
    ) -> float:
        if initial_temperature is None:
            initial_temperature = current_temperature
        return initial_temperature / (1 + self.alpha * step)
