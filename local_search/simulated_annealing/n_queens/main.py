from ..simulated_annealing import SimulatedAnnealing
import random
from .state import State


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

    print(f"--- Solving {N}-Queens Problem with Simulated Annealing ---")
    problem = NQueensProblem(N)

    algorithms = {
        "Simulated Annealing (Exponential Cooling)": {
            "class": SimulatedAnnealing,
            "params": {
                "optimum": "min",
                "cooling_type": "exponential",
                "initial_temperature": 1000,
                "cooling_rate": 0.95,
                "min_temperature": 1e-8,
                "max_steps": 10000,
            },
        },
        "Simulated Annealing (Linear Cooling)": {
            "class": SimulatedAnnealing,
            "params": {
                "optimum": "min",
                "cooling_type": "linear",
                "initial_temperature": 1000,
                "min_temperature": 1e-8,
                "max_steps": 10000,
            },
        },
        "Simulated Annealing (Fast Exponential Cooling)": {
            "class": SimulatedAnnealing,
            "params": {
                "optimum": "min",
                "cooling_type": "exponential",
                "initial_temperature": 1000,
                "cooling_rate": 0.99,
                "min_temperature": 1e-8,
                "max_steps": 10000,
            },
        },
    }

    for name, config in algorithms.items():
        print(f"\n=== {name} ===")

        initial_state = problem.generate_random_initial_state()
        print(f"Initial State ({name}):")
        print(initial_state)

        solver = config["class"](initial_state, **config["params"])
        final_state = solver.search()

        print(f"\nFinal State ({name}):")
        print(final_state)
        print(f"Final Temperature: {solver.temperature:.2e}")
        print(f"Steps taken: {solver.current_step}")

        if final_state.is_goal():
            print("Success! Goal state found.")
        else:
            print("Did not find goal state within temperature/step limits.")
