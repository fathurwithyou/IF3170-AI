from .hill_climb import HillClimb


class RandomRestart:
    def __init__(self, problem, hill_climb_variant=HillClimb, max_restarts=1000):
        self.problem = problem
        self.hill_climb_variant = hill_climb_variant
        self.max_restarts = max_restarts

    def search(self):
        best_state_found = None
        for i in range(self.max_restarts):
            initial_state = self.problem.generate_random_initial_state()
            hc_solver = self.hill_climb_variant(initial_state)
            final_state = hc_solver.search()

            if final_state and final_state.is_goal():
                return final_state

            if best_state_found is None or final_state.value < best_state_found.value:
                best_state_found = final_state

        return best_state_found

    def step(self):
        """Dummy step method for compatibility"""
        return False
