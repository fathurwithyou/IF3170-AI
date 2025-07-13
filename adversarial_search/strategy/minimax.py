from .strategy import Strategy
from ..games import Game


class MinimaxStrategy(Strategy):
    """Minimax algorithm implementation"""

    def solve(self, game: Game, depth: int, maximizing: bool) -> int:
        """Solve using minimax algorithm"""
        if game.is_terminal():
            return game.evaluate()

        if maximizing:
            max_eval = float("-inf")
            for move in game.get_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval_score = self.solve(game_copy, depth + 1, False)
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float("inf")
            for move in game.get_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval_score = self.solve(game_copy, depth + 1, True)
                min_eval = min(min_eval, eval_score)
            return min_eval

    def find_best_move(self, game: Game, depth: int):
        """Find best move using minimax"""
        best_score = float("-inf")
        best_move = None

        for move in game.get_moves():
            game_copy = game.copy()
            game_copy.make_move(move)
            score = self.solve(game_copy, depth + 1, False)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move
