from .hill_climb import HillClimb


class Sideways(HillClimb):
    def __init__(self, initial_state, max_steps=1000, sideways_limit=100, **kwargs):
        super().__init__(initial_state, max_steps, **kwargs)
        self.sideways_limit = sideways_limit
        self.sideways_count = 0

    def step(self):
        neighbors = self.state.neighbors
        if not neighbors:
            return False

        best_neighbor = min(neighbors, key=lambda x: x.value)

        current_value = self.state.value

        if best_neighbor.value < current_value:
            self.state = best_neighbor
            self.sideways_count = 0
            return True
        elif (
            best_neighbor.value == current_value
            and self.sideways_count < self.sideways_limit
        ):
            self.state = best_neighbor
            self.sideways_count += 1
            return True

        return False
