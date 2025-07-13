from .game import Game
from ..adversarial_search import AdversarialSearch


class TicTacToe(Game):
    """Simple TicTacToe implementation"""

    def __init__(self, board=None, player="X"):
        self.board = board or [[" " for _ in range(3)] for _ in range(3)]
        self.player = player

    def is_terminal(self) -> bool:
        """Check if game is over"""
        return self._check_winner() is not None or self._is_full()

    def get_moves(self) -> list:
        """Get all possible moves (row, col)"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    moves.append((i, j))
        return moves

    def make_move(self, move):
        """Make a move at (row, col)"""
        row, col = move
        self.board[row][col] = self.player
        self.player = "O" if self.player == "X" else "X"

    def evaluate(self) -> int:
        """Evaluate board position"""
        winner = self._check_winner()
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        else:
            return 0

    def copy(self):
        """Create a copy of the game state"""
        new_board = [row[:] for row in self.board]
        return TicTacToe(new_board, self.player)

    def _check_winner(self):
        """Check for winner"""
        # Rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def _is_full(self):
        """Check if board is full"""
        return all(cell != " " for row in self.board for cell in row)

    def display(self):
        """Display the board"""
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("---------")


def play_interactive(strategy_name: str = "alphabeta"):
    """Interactive game with strategy selection"""
    game = TicTacToe()
    ai = AdversarialSearch(game)
    ai.set_strategy(strategy_name)

    print(f"TicTacToe Game (Strategy: {ai.get_strategy_name()})")
    print("You are X, AI is O")

    while not game.is_terminal():
        game.display()
        print()

        if game.player == "X":
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))

                if (row, col) not in game.get_moves():
                    print("Invalid move!")
                    continue

                game.make_move((row, col))
            except (ValueError, IndexError):
                print("Invalid input!")
                continue
        else:
            print("AI thinking...")
            move = ai.best_move()
            print(f"AI plays: {move}")
            game.make_move(move)

    game.display()
    winner = game._check_winner()
    if winner:
        print(f"\nGame Over! {winner} wins!")
    else:
        print("\nGame Over! It's a tie!")


if __name__ == "__main__":
    import sys
    from ..strategy_parser import StrategyParser

    strategy_name = "alphabeta"

    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            parser = StrategyParser()
            available = parser.get_available_strategies()
            print("TicTacToe Game with Strategy Selection")
            print("Usage: uv run -m adversarial_search.games.tictactoe [strategy]")
            print(f"Available strategies: {', '.join(available)}")
            print("Example: uv run -m adversarial_search.games.tictactoe minimax")
            sys.exit(0)
        else:
            strategy_name = sys.argv[1]

    try:
        play_interactive(strategy_name)
    except ValueError as e:
        print(f"Error: {e}")
        parser = StrategyParser()
        available = parser.get_available_strategies()
        print(f"Available strategies: {', '.join(available)}")
