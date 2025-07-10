from abc import ABC, abstractmethod


class CoolingStrategy(ABC):
    """
    Abstract base class for cooling strategies in simulated annealing.
    """

    def __init__(self, initial_temperature, min_temperature, max_steps):
        """
        Initialize cooling strategy.

        Args:
            initial_temperature: Starting temperature
            min_temperature: Minimum temperature threshold
            max_steps: Maximum number of steps for the algorithm
        """
        self.initial_temperature = initial_temperature
        self.min_temperature = min_temperature
        self.max_steps = max_steps
        self.current_temperature = initial_temperature

    @abstractmethod
    def cool_down(self):
        """
        Apply cooling schedule to reduce temperature.
        Must be implemented by subclasses.
        """
        pass

    def reset(self):
        """Reset temperature to initial value."""
        self.current_temperature = self.initial_temperature

    @property
    def temperature(self):
        """Get current temperature."""
        return self.current_temperature
