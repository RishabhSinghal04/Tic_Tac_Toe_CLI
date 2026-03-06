from board import check_winner
import random


def ai_move_medium(board: list[list[str]], ai_player: str, human_player: str) -> int:
    n: int = len(board)
    num_of_cells: int = n * n

    # try to win
    # check for empty cell and assign one if found
    # return that position where AI wins
    for position in range(1, num_of_cells + 1):
        row, col = divmod(position - 1, n)
        if board[row][col] == "":
            board[row][col] = ai_player
            if check_winner(board, ai_player):
                board[row][col] = ""
                return position
            board[row][col] = ""

    # block opponent
    # check for empty cell and assign one to human player if found
    # return that position where opponent will win
    for position in range(1, num_of_cells + 1):
        row, col = divmod(position - 1, n)
        if board[row][col] == "":
            board[row][col] = human_player
            if check_winner(board, human_player):
                board[row][col] = ""
                return position
            board[row][col] = ""

    # strategic fallback
    centers: list[int] = _get_center_positions(n)
    for centre in centers:
        row, col = divmod(centre - 1, n)
        if board[row][col] == "":
            return centre
        
    # corners
    corners: list[int] = [1, n, num_of_cells - n + 1, num_of_cells]
    for corner in corners:
        row, col = divmod(corner - 1, n)
        if board[row][col] == "":
            return corner

    # random move
    available: list[int] = [
        position
        for position in range(1, num_of_cells + 1)
        if board[(position - 1) // n][(position - 1) % n] == ""
    ]
    return random.choice(available)


def _get_center_positions(n: int) -> list[int]:
    num_of_cells: int = n * n
    if n % 2 == 1:
        return [(num_of_cells + 1) // 2]

    mid: int = n // 2
    return [
        (mid - 1) * n + mid,
        (mid - 1) + n + mid + 1,
        mid * n + mid,
        mid * n + mid + 1,
    ]
