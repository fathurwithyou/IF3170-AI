import random
from .hill_climb import HillClimb


class Stochastic(HillClimb):
    def __init__(self, initial_state, max_steps=1000, **kwargs):
        super().__init__(initial_state, max_steps, **kwargs)

    def step(self):
        neighbors = self.state.neighbors
        if not neighbors:
            return False

        random_neighbor = random.choice(neighbors)

        if random_neighbor.value < self.state.value:
            self.state = random_neighbor

        return True
