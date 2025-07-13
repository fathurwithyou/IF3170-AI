from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    """Base interface for local search algorithms"""

    def __init__(self, initial_state, **kwargs):
        self.state = initial_state
        self.initial_state = initial_state

    @abstractmethod
    def search(self):
        """Execute the search algorithm and return final state"""
        pass

    @abstractmethod
    def step(self):
        """Perform one step of the algorithm"""
        pass

    def reset(self):
        """Reset to initial state"""
        self.state = self.initial_state
