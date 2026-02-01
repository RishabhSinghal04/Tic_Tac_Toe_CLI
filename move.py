from board import check_winner, display_board, total_cells
from player import switch_player
from player.AI import ai_move_hard, ai_move_medium
from user_input import user_input


def move(
    board,
    players: dict,
    ai_difficulty: str = "medium",
    current_player: str = "X",
    turns: int = 1,
) -> str:
    """
    Run the game loop until a winner is found or the board is full.

    Args:
        board (list[list[str]]): The game board.
        players (dict): Mapping of symbols ("X", "O") to "human" or "ai".
        ai_difficulty (str): Difficulty level for AI ("medium" or "hard").
        current_player (str): Symbol of the starting player.
        turns (int): Current turn number.

    Returns:
        str: The winner symbol ("X" or "O"), or "" if no winner.
    """
    n = len(board)
    num_of_cells = total_cells(board)

    while turns <= num_of_cells:
        position = _get_position(
            board, players, ai_difficulty, current_player, num_of_cells
        )
        mark_row, mark_col = divmod(position - 1, n)

        """
        0,1  0,2  1,0
        1,1  1,2  2,0
        2,1  2,2  3,0

        position - 1 then perform floor division, modulo by 3
        """

        if _is_cell_available(board, mark_row, mark_col):
            _apply_move(board, current_player, mark_row, mark_col)

            display_board(board)
            if check_winner(board, current_player):
                return current_player

            turns += 1
            current_player = switch_player(current_player)
        else:
            print("Not Available! Try Again!")

    return ""


def _get_position(
    board, players: dict, ai_difficulty: str, current_player: str, num_of_cells: int
) -> int:
    return (
        _ai_move(board, ai_difficulty, current_player)
        if players[current_player] == "ai".casefold()
        else user_input("Player " + current_player, num_of_cells)
    )


def _ai_move(board, ai_difficulty: str, current_player: str) -> int:
    opponent = switch_player(current_player)
    return (
        ai_move_medium(board, current_player, opponent)
        if ai_difficulty == "medium".casefold()
        else ai_move_hard(board, current_player, opponent)
    )


def _is_cell_available(board, row: int, col: int) -> bool:
    return board[row][col] == ""


def _apply_move(board, player: str, row: int, col: int) -> None:
    board[row][col] = player
