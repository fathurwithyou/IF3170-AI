class State:
    """
    Represents a state in the N-Queens problem.
    board_config: A tuple where index is column and value is row.
    """

    def __init__(self, board_config):
        self.board_config = board_config
        self.value = self._calculate_value()

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
                if self.board_config[i] == self.board_config[j] or abs(
                    self.board_config[i] - self.board_config[j]
                ) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs

    def is_goal(self):
        """Checks if the current state is a goal state (0 attacking pairs)."""
        return self.value == 0

    @property
    def neighbors(self):
        """
        Generates neighbor states by moving one queen to a different row within its column.
        """
        n = len(self.board_config)
        neighbors_list = []
        for col in range(n):
            original_row = self.board_config[col]
            for row in range(n):
                if row != original_row:
                    new_board_config = list(self.board_config)
                    new_board_config[col] = row
                    neighbors_list.append(State(tuple(new_board_config)))
        return neighbors_list

    def __str__(self):
        """String representation for printing the board."""
        n = len(self.board_config)
        board_str = ""
        for row in range(n):
            line = ""
            for col in range(n):
                if self.board_config[col] == row:
                    line += " Q "
                else:
                    line += " . "
            board_str += line + "\n"
        board_str += f"Attacks: {self.value}"
        return board_str
