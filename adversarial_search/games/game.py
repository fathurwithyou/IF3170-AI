from abc import ABC, abstractmethod


class Game(ABC):
    """Simple game interface"""

    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @abstractmethod
    def get_moves(self) -> list:
        pass

    @abstractmethod
    def make_move(self, move):
        pass

    @abstractmethod
    def evaluate(self) -> int:
        pass
