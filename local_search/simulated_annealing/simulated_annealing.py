from .minimization_simulated_annealing import MinimizationSimulatedAnnealing
from .maximization_simulated_annealing import MaximizationSimulatedAnnealing
from .cooling import ExponentialCooling, LinearCooling


class SimulatedAnnealing:
    """
    Factory class for creating SimulatedAnnealing instances with specified optimization and cooling.
    """

    def __new__(
        cls,
        initial_state,
        optimum="min",
        cooling_type="exponential",
        initial_temperature=1000,
        cooling_rate=0.95,
        min_temperature=1e-8,
        max_steps=10000,
    ):
        """
        Create SimulatedAnnealing instance with specified optimization and cooling.

        Args:
            initial_state: Initial state for the search
            optimum: 'min' for minimization, 'max' for maximization
            cooling_type: 'exponential' or 'linear' cooling schedule
            initial_temperature: Starting temperature
            cooling_rate: Rate of temperature decrease (for exponential cooling)
            min_temperature: Minimum temperature threshold
            max_steps: Maximum number of search steps

        Returns:
            Configured SimulatedAnnealing instance
        """
        if optimum not in ["min", "max"]:
            raise ValueError("optimum must be 'min' or 'max'")

        if cooling_type not in ["exponential", "linear"]:
            raise ValueError("cooling_type must be 'exponential' or 'linear'")

        if cooling_type == "exponential":
            cooler = ExponentialCooling(
                initial_temperature, min_temperature, max_steps, cooling_rate
            )
        else:
            cooler = LinearCooling(initial_temperature, min_temperature, max_steps)

        if optimum == "min":
            base_class = MinimizationSimulatedAnnealing
        else:
            base_class = MaximizationSimulatedAnnealing

        class SimulatedAnnealingWithCooling(base_class):
            def __init__(self, initial_state, cooler):
                super().__init__(
                    initial_state,
                    cooler.initial_temperature,
                    0,
                    cooler.min_temperature,
                    cooler.max_steps,
                )
                self.cooler = cooler

            def cool_down(self):
                self.cooler.cool_down()
                self.temperature = self.cooler.temperature

            def search(self):
                self.cooler.reset()
                self.temperature = self.cooler.temperature
                return super().search()

        return SimulatedAnnealingWithCooling(initial_state, cooler)
