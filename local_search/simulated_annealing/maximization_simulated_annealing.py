import math
from .simulated_annealing_base import SimulatedAnnealing


class MaximizationSimulatedAnnealing(SimulatedAnnealing):
    """
    Simulated Annealing for maximization problems.
    Accepts worse moves (lower values) with decreasing probability.
    """

    def acceptance_probability(self, energy_delta, temperature):
        """
        Calculate probability of accepting a worse move for a MAXIMIZATION problem.
        E = neighbor.value - current.value
        If E > 0 (better state): always accept
        If E < 0 (worse state): accept with probability e^(E/T)
        """
        if energy_delta > 0:
            return 1.0
        if temperature <= 0:
            return 0.0
        return math.exp(energy_delta / temperature)
