from .local_search_parser import LocalSearchParser


class LocalSearch:
    """Local search using algorithm parser pattern"""

    def __init__(
        self, initial_state, algorithm=None, algorithm_name: str = None, **kwargs
    ):
        self.initial_state = initial_state

        if algorithm is not None:
            self.algorithm = algorithm
        elif algorithm_name is not None:
            parser = LocalSearchParser()
            self.algorithm = parser.parse(
                algorithm_name, initial_state=initial_state, **kwargs
            )
        else:
            parser = LocalSearchParser()
            self.algorithm = parser.parse(
                "hill_climb", initial_state=initial_state, **kwargs
            )

    def search(self):
        """Execute the search algorithm"""
        return self.algorithm.search()

    def step(self):
        """Perform one step of the algorithm"""
        return self.algorithm.step()

    def reset(self):
        """Reset the search to initial state"""
        self.algorithm.reset()

    def set_algorithm(self, algorithm_name: str, **kwargs):
        """Change algorithm by name"""
        parser = LocalSearchParser()
        self.algorithm = parser.parse(
            algorithm_name, initial_state=self.initial_state, **kwargs
        )

    def get_algorithm_name(self) -> str:
        """Get current algorithm name"""
        return self.algorithm.__class__.__name__

    def get_current_state(self):
        """Get current state"""
        return self.algorithm.state
