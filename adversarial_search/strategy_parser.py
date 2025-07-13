from .strategy.minimax import MinimaxStrategy
from .strategy.alpha_beta import AlphaBetaStrategy
from .strategy.strategy import Strategy


class StrategyParser:
    """Parser to create strategy instances from string names"""

    def __init__(self):
        self._strategies = {"minimax": MinimaxStrategy, "alphabeta": AlphaBetaStrategy}

    def parse(self, strategy_name: str) -> Strategy:
        """Parse strategy name and return strategy instance"""
        strategy_name = strategy_name.lower().strip()

        if strategy_name not in self._strategies:
            available = ", ".join(self._strategies.keys())
            raise ValueError(
                f"Unknown strategy '{strategy_name}'. Available: {available}"
            )

        strategy_class = self._strategies[strategy_name]
        return strategy_class()

    def get_available_strategies(self) -> list:
        """Get list of available strategy names"""
        return list(self._strategies.keys())

    def register_strategy(self, name: str, strategy_class):
        """Register a new strategy"""
        self._strategies[name.lower()] = strategy_class
