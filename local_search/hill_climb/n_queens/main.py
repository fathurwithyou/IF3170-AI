from ..hill_climb import BasicHillClimb
from .sideways import Sideways
from .stochastic import Stochastic
from .random_restart import RandomRestart
from .state import State
import random


class NQueensProblem:
    """
    Represents the N-Queens problem, capable of generating random initial states.
    """

    def __init__(self, n):
        self.n = n

    def generate_random_initial_state(self):
        """Generates a random initial state for the N-Queens problem."""

        board_config = tuple(random.randint(0, self.n - 1) for _ in range(self.n))
        return State(board_config)


if __name__ == "__main__":
    N = 8

    print(f"--- Solving {N}-Queens Problem ---")
    problem = NQueensProblem(N)

    algorithms = {
        "Basic Hill Climbing": {
            "class": BasicHillClimb,
            "params": {"max_steps": 10000},
            "needs_initial_state": True,
        },
        "Hill Climbing with Sideways Moves": {
            "class": Sideways,
            "params": {"sideways_limit": 50},
            "needs_initial_state": True,
        },
        "Stochastic Hill Climbing": {
            "class": Stochastic,
            "params": {"max_steps": 10000},
            "needs_initial_state": True,
        },
        "Random Restart Hill Climbing": {
            "class": RandomRestart,
            "params": {"hill_climb_variant": BasicHillClimb, "max_restarts": 100},
            "needs_initial_state": False,
        },
        "Random Restart Hill Climbing with Sideways Variant": {
            "class": RandomRestart,
            "params": {"hill_climb_variant": Sideways, "max_restarts": 50},
            "needs_initial_state": False,
        },
    }

    for name, config in algorithms.items():
        print(f"\n=== {name} ===")

        if config["needs_initial_state"]:
            initial_state = problem.generate_random_initial_state()
            print(f"Initial State ({name}):")
            print(initial_state)
            solver = config["class"](initial_state, **config["params"])
            final_state = solver.search()
            print(f"\nFinal State ({name}):")
            print(final_state)
            if final_state.is_goal():
                print("Success! Goal state found.")
            else:
                print("Stuck in a local optimum or reached max steps.")
        else:
            solver = config["class"](problem, **config["params"])
            final_state = solver.search()
            print(f"\nFinal State ({name}):")
            print(final_state)
            if final_state and final_state.is_goal():
                print("Success! Goal state found.")
            else:
                print("Did not find a goal state after all restarts.")
