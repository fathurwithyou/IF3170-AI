from abc import ABC, abstractmethod
from ..games import Game


class Strategy(ABC):
    """Abstract strategy for adversarial search"""

    @abstractmethod
    def solve(self, game: Game, depth: int, maximizing: bool) -> int:
        """Solve the game using specific algorithm"""
        pass

    @abstractmethod
    def find_best_move(self, game: Game, depth: int):
        """Find the best move for the current player"""
        pass
