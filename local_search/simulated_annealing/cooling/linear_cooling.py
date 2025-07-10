from .cooling_strategy import CoolingStrategy


class LinearCooling(CoolingStrategy):
    """
    Linear cooling strategy for simulated annealing.
    Temperature decreases linearly: T = T - temp_decrease
    """

    def __init__(self, initial_temperature, min_temperature, max_steps):
        """
        Initialize linear cooling strategy.

        Args:
            initial_temperature: Starting temperature
            min_temperature: Minimum temperature threshold
            max_steps: Maximum number of steps for the algorithm
        """
        super().__init__(initial_temperature, min_temperature, max_steps)
        self.temp_decrease = (initial_temperature - min_temperature) / max_steps

    def cool_down(self):
        """Apply linear cooling schedule."""
        self.current_temperature -= self.temp_decrease
        if self.current_temperature < self.min_temperature:
            self.current_temperature = self.min_temperature
