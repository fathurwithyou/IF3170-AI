from .cooling_strategy import CoolingStrategy


class ExponentialCooling(CoolingStrategy):
    """
    Exponential cooling strategy for simulated annealing.
    Temperature decreases exponentially: T = T * cooling_rate
    """

    def __init__(
        self, initial_temperature, min_temperature, max_steps, cooling_rate=0.95
    ):
        """
        Initialize exponential cooling strategy.

        Args:
            initial_temperature: Starting temperature
            min_temperature: Minimum temperature threshold
            max_steps: Maximum number of steps for the algorithm
            cooling_rate: Rate of temperature decrease (0 < cooling_rate < 1)
        """
        super().__init__(initial_temperature, min_temperature, max_steps)
        if not (0 < cooling_rate < 1):
            raise ValueError("cooling_rate must be between 0 and 1")
        self.cooling_rate = cooling_rate

    def cool_down(self):
        """Apply exponential cooling schedule."""
        self.current_temperature *= self.cooling_rate
        if self.current_temperature < self.min_temperature:
            self.current_temperature = self.min_temperature
