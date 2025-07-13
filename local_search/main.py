from .games.n_queens import solve_n_queens, interactive_demo
from .local_search_parser import LocalSearchParser


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            parser = LocalSearchParser()
            available = parser.get_available_algorithms()
            print("Local Search Main Entry Point")
            print("Usage: uv run -m local_search.main [options]")
            print()
            print("Available games:")
            print("  n_queens  - N-Queens problem solver")
            print()
            print("Examples:")
            print("  uv run -m local_search.main n_queens hill_climb 8 5")
            print("  uv run -m local_search.games.n_queens simulated_annealing 10")
            print("  uv run -m local_search.games.n_queens --help")
            print()
            print(f"Available algorithms: {', '.join(available)}")
            sys.exit(0)
        elif sys.argv[1] == "n_queens":
            sys.argv = sys.argv[:1] + sys.argv[2:]
            if len(sys.argv) > 1:
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
            else:
                interactive_demo()
        else:
            print(f"Unknown game: {sys.argv[1]}")
            print("Available games: n_queens")
            print("Use --help for more information")
    else:
        print("Local Search Framework")
        print("Use --help for usage information")
        print("Quick start: uv run -m local_search.games.n_queens")
