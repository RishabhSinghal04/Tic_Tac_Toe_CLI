def create_board(n: int) -> list[list[str]]:
    """
    Creates a nXn board for the game.

    Args:
        n (int): lenght of the game board
    """
    board: list[list[str]] = [["" for _ in range(n)] for _ in range(n)]
    return board
