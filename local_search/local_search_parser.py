from .search_algorithm import SearchAlgorithm
from .hill_climb.hill_climb import BasicHillClimb
from .hill_climb.sideways import Sideways
from .hill_climb.stochastic import Stochastic
from .hill_climb.random_restart import RandomRestart
from .simulated_annealing.maximization_simulated_annealing import (
    MaximizationSimulatedAnnealing,
)
from .simulated_annealing.minimization_simulated_annealing import (
    MinimizationSimulatedAnnealing,
)
from .simulated_annealing.cooling_strategy import (
    ExponentialCooling,
    LinearCooling,
    LogarithmicCooling,
    InverseCooling,
)


class LocalSearchParser:
    """Parser to create local search algorithm instances from string names"""

    def __init__(self):
        self._algorithms = {
            "hill_climb": BasicHillClimb,
            "basic_hill_climb": BasicHillClimb,
            "sideways": Sideways,
            "sideways_hill_climb": Sideways,
            "stochastic": Stochastic,
            "stochastic_hill_climb": Stochastic,
            "random_restart": self._create_random_restart,
            "minimization_sa": MinimizationSimulatedAnnealing,
            "maximization_sa": MaximizationSimulatedAnnealing,
        }

        self._cooling_strategies = {
            "exponential": ExponentialCooling,
            "linear": LinearCooling,
            "logarithmic": LogarithmicCooling,
            "inverse": InverseCooling,
        }

    def parse(self, algorithm_name: str, **kwargs) -> SearchAlgorithm:
        """Parse algorithm name and return algorithm instance"""
        algorithm_name = algorithm_name.lower().strip()

        if algorithm_name not in self._algorithms:
            available = ", ".join(self._algorithms.keys())
            raise ValueError(
                f"Unknown algorithm '{algorithm_name}'. Available: {available}"
            )

        algorithm_class_or_func = self._algorithms[algorithm_name]

        if callable(algorithm_class_or_func) and not hasattr(
            algorithm_class_or_func, "__bases__"
        ):
            return algorithm_class_or_func(**kwargs)
        else:
            return algorithm_class_or_func(**kwargs)

    def _create_random_restart(
        self, initial_state, hill_climb_variant="basic_hill_climb", **kwargs
    ):
        """Create RandomRestart with specified hill climb variant"""
        if isinstance(hill_climb_variant, str):
            variant_class = self._algorithms.get(hill_climb_variant, BasicHillClimb)
        else:
            variant_class = hill_climb_variant

        class ProblemWrapper:
            def __init__(self, initial_state):
                self.initial_state = initial_state

            def generate_random_initial_state(self):
                return self.initial_state

        problem = ProblemWrapper(initial_state)
        return RandomRestart(problem, variant_class, **kwargs)

    def get_available_algorithms(self) -> list:
        """Get list of available algorithm names"""
        return list(self._algorithms.keys())

    def get_available_cooling_strategies(self) -> list:
        """Get list of available cooling strategies for SA"""
        return list(self._cooling_strategies.keys())

    def register_algorithm(self, name: str, algorithm_class):
        """Register a new algorithm"""
        self._algorithms[name.lower()] = algorithm_class
