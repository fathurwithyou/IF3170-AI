from .strategy import Strategy
from ..games import Game


class AlphaBetaStrategy(Strategy):
    """Alpha-Beta pruning algorithm implementation"""

    def solve(
        self,
        game: Game,
        depth: int,
        maximizing: bool,
        alpha: float = float("-inf"),
        beta: float = float("inf"),
    ) -> int:
        """Solve using alpha-beta pruning algorithm"""
        if depth == 0 or game.is_terminal():
            return game.evaluate()

        if maximizing:
            max_eval = float("-inf")
            for move in game.get_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval_score = self.solve(game_copy, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = float("inf")
            for move in game.get_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval_score = self.solve(game_copy, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def find_best_move(self, game: Game, depth: int):
        """Find best move using alpha-beta pruning"""
        best_score = float("-inf")
        best_move = None
        alpha = float("-inf")
        beta = float("inf")

        for move in game.get_moves():
            game_copy = game.copy()
            game_copy.make_move(move)
            score = self.solve(game_copy, depth - 1, False, alpha, beta)

            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)

        return best_move
