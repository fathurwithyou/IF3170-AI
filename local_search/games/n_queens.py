import random
from ..local_search import LocalSearch
from ..local_search_parser import LocalSearchParser


class NQueensState:
    """
    Represents a state in the N-Queens problem.
    board_config: A tuple where index is column and value is row.
    """

    def __init__(self, board_config):
        self.board_config = board_config
        self.value = self._calculate_value()

    @classmethod
    def random(cls, n):
        """Create a random N-Queens state"""
        board_config = tuple(random.randint(0, n - 1) for _ in range(n))
        return cls(board_config)

    def _calculate_value(self):
        """
        Calculates the number of attacking pairs of queens.
        A lower value (closer to 0) indicates a better state.
        The goal state has a value of 0.
        """
        n = len(self.board_config)
        attacking_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Same row
                if self.board_config[i] == self.board_config[j]:
                    attacking_pairs += 1
                # Same diagonal
                if abs(self.board_config[i] - self.board_config[j]) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs

    @property
    def neighbors(self):
        """
        Generates all neighboring states by moving one queen to a different row.
        """
        neighbors = []
        n = len(self.board_config)
        for col in range(n):
            for row in range(n):
                if row != self.board_config[col]:
                    new_config = list(self.board_config)
                    new_config[col] = row
                    neighbors.append(NQueensState(tuple(new_config)))
        return neighbors

    def is_goal(self):
        """
        Returns True if this is a goal state (no attacking pairs).
        """
        return self.value == 0

    def display(self):
        """Display the N-Queens board"""
        n = len(self.board_config)
        board = [["." for _ in range(n)] for _ in range(n)]

        for col, row in enumerate(self.board_config):
            board[row][col] = "Q"

        for row in board:
            print("  " + " ".join(row))

    def __str__(self):
        return f"NQueens({self.board_config}, conflicts={self.value})"

    def __repr__(self):
        return self.__str__()


def solve_n_queens(
    n=8, algorithm_name="hill_climb", max_steps=1000, verbose=True, **kwargs
):
    """Solve N-Queens using specified algorithm"""
    if verbose:
        print(f"Solving {n}-Queens with {algorithm_name}")
        print("=" * 40)

    initial_state = NQueensState.random(n)
    search = LocalSearch(
        initial_state, algorithm_name=algorithm_name, max_steps=max_steps, **kwargs
    )

    if verbose:
        print(f"Algorithm: {search.get_algorithm_name()}")
        print(f"Initial conflicts: {initial_state.value}")
        print(f"Max steps: {max_steps}")
        print("Running search...")

    # Run search
    final_state = search.search()

    if verbose:
        print(f"Final conflicts: {final_state.value}")
        print(f"Solution found: {final_state.is_goal()}")

        if final_state.is_goal():
            print("\n  Solution found!")
            print("Board configuration:")
            final_state.display()
        else:
            print(f"\n✗ No solution found within {max_steps} steps")
            print("Best board configuration:")
            final_state.display()

    return final_state


def main():
    """Main function for command line execution"""
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            parser = LocalSearchParser()
            available = parser.get_available_algorithms()
            print("N-Queens Local Search with Algorithm Parser")
            print(
                "Usage: uv run -m local_search.games.n_queens [algorithm] [size] [max_steps]"
            )
            print(f"Available algorithms: {', '.join(available)}")
            print("Examples:")
            print("  uv run -m local_search.games.n_queens hill_climb 8 1000")
            print("  uv run -m local_search.games.n_queens simulated_annealing 10")
            print("  uv run -m local_search.games.n_queens sideways")
            sys.exit(0)
        else:
            algorithm_name = sys.argv[1] if len(sys.argv) > 1 else "hill_climb"
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
            max_attempts = int(sys.argv[3]) if len(sys.argv) > 3 else 10

            try:
                solve_n_queens(n, algorithm_name, max_attempts)
            except ValueError as e:
                print(f"Error: {e}")
                parser = LocalSearchParser()
                available = parser.get_available_algorithms()
                print(f"Available algorithms: {', '.join(available)}")


if __name__ == "__main__":
    main()
