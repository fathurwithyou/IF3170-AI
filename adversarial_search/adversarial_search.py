from .games import Game
from .strategy_parser import StrategyParser


class AdversarialSearch:
    """Adversarial search using strategy pattern"""

    def __init__(self, game: Game):
        self.game = game

    def best_move(self, depth: int = 0):
        """Find best move using selected strategy"""
        return self.strategy.find_best_move(self.game, depth)

    def set_strategy(self, strategy_name: str):
        """Change strategy by name"""
        parser = StrategyParser()
        self.strategy = parser.parse(strategy_name)

    def get_strategy_name(self) -> str:
        """Get current strategy name"""
        return self.strategy.__class__.__name__
