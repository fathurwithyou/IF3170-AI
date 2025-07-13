from .games import Game
from .strategy.strategy import Strategy


class AdversarialSearch:
    """Adversarial search using strategy pattern"""

    def __init__(self, game: Game, strategy: Strategy):
        self.game = game
        self.strategy = strategy

    def best_move(self, depth: int = 0):
        """Find best move using selected strategy"""
        return self.strategy.find_best_move(self.game, depth)
