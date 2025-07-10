import random
from ..hill_climb import HillClimb


class Stochastic(HillClimb):
    def __init__(self, state, max_steps=1000):
        super().__init__(state, max_steps)

    def step(self):
        neighbors = self.state.neighbors
        if not neighbors:
            return False

        random_neighbor = random.choice(neighbors)

        if random_neighbor.value < self.state.value:
            self.state = random_neighbor

        return True
