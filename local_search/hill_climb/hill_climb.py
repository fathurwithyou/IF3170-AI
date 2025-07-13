from abc import abstractmethod
from ..search_algorithm import SearchAlgorithm


class HillClimb(SearchAlgorithm):
    """
    Base class for Hill Climbing algorithms.
    Assumes `state` has `neighbors` property and `value` attribute.
    """

    def __init__(self, initial_state, max_steps=1000, **kwargs):
        super().__init__(initial_state, **kwargs)
        self.max_steps = max_steps
        self.current_step = 0

    @abstractmethod
    def step(self):
        """
        Performs one step of the hill climbing algorithm.
        This method must be implemented by subclasses.
        Returns True if a move was made, False otherwise (e.g., at a local optimum).
        """
        pass

    def search(self):
        """
        Executes the hill climbing search.
        Returns the final state (either a goal or a local optimum).
        """
        self.current_step = 0
        while self.current_step < self.max_steps:
            if self.state.is_goal():
                return self.state

            made_move = self.step()
            if not made_move:
                return self.state

            self.current_step += 1
        return self.state


class BasicHillClimb(HillClimb):
    """
    Basic Hill Climbing implementation that moves to the best neighbor.
    """

    def step(self):
        """
        Performs one step of basic hill climbing.
        Returns True if a move was made, False if stuck at local optimum.
        """
        current_value = self.state.value
        best_neighbor = None
        best_value = current_value

        for neighbor in self.state.neighbors:
            if neighbor.value > best_value:
                best_value = neighbor.value
                best_neighbor = neighbor

        if best_neighbor is not None:
            self.state = best_neighbor
            return True

        return False
