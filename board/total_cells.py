def total_cells(board) -> int:
    """
    Total cells present in the board

    Args:
        board (list[list[str]]): The game board represented as a 2D list.
        
    Returns:
        int: Total number of cells in the board.
    """
    return len(board) * len(board[0])
