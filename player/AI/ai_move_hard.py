from .minimax import minimax
import random


def ai_move_hard(board, ai_player: str, human_player: str) -> int:
    n = len(board)
    num_of_cells = n * n
    best_score = -float("inf")
    best_moves = []

    for position in range(1, num_of_cells + 1):
        row, col = divmod(position - 1, n)
        if board[row][col] == "":
            board[row][col] = ai_player
            score = minimax(board, 0, False, ai_player, human_player)
            board[row][col] = ""
            if score > best_score:
                best_score = score
                best_moves = [position]
            elif score == best_score:
                best_moves.append(position)

    return random.choice(best_moves)
