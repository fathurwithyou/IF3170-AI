import random
from abc import abstractmethod
from ..search_algorithm import SearchAlgorithm
from .cooling_strategy import ExponentialCooling


class SimulatedAnnealing(SearchAlgorithm):
    """
    Simulated Annealing algorithm implementation.
    Uses temperature-based probability to accept worse moves.
    """

    def __init__(
        self,
        initial_state,
        initial_temperature=1000,
        cooling_rate=0.95,
        min_temperature=1e-8,
        max_steps=10000,
        cooling_strategy=None,
        **kwargs,
    ):
        super().__init__(initial_state, **kwargs)
        self.initial_temperature = initial_temperature
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        self.max_steps = max_steps
        self.current_step = 0

        if cooling_strategy is not None:
            self.cooling_strategy = cooling_strategy
        else:
            self.cooling_strategy = ExponentialCooling(cooling_rate)

    @abstractmethod
    def acceptance_probability(self, energy_delta, temperature):
        """
        Calculate probability of accepting a worse move.
        Must be implemented by subclasses for minimization or maximization.
        """
        pass

    def cool_down(self):
        """Apply cooling strategy to reduce temperature."""
        self.temperature = self.cooling_strategy.cool(
            self.temperature,
            self.current_step,
            initial_temperature=self.initial_temperature,
        )

    def step(self):
        """
        Performs one step of simulated annealing.
        Returns True if a move was made, False if no neighbors available.
        """
        neighbors = self.state.neighbors
        if not neighbors:
            return False

        current_value = self.state.value
        neighbor = random.choice(neighbors)
        neighbor_value = neighbor.value

        energy_delta = neighbor_value - current_value
        probability = self.acceptance_probability(energy_delta, self.temperature)

        if random.random() < probability:
            self.state = neighbor

        return True

    def search(self):
        """
        Executes the simulated annealing search.
        Returns the final state found.
        """
        self.current_step = 0
        self.temperature = self.initial_temperature

        while (
            self.current_step < self.max_steps
            and self.temperature > self.min_temperature
        ):
            if self.state.is_goal():
                return self.state

            made_move = self.step()
            if not made_move:
                break

            self.cool_down()
            self.current_step += 1

        return self.state
