def create_board(n: int):
    """
    Creates a nXn board for the game.

    Args:
        n (int): lenght of the game board
    """
    board = [["" for _ in range(n)] for _ in range(n)]
    return board
