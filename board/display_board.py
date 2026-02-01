def display_board(board) -> None:
    """
    Display the game board.

    Args:
        board (list[list[str]]): The game board represented as a 2D list.
    """
    cols = len(board[0])
    # Each cell takes up 3 characters, plus 1 for the border
    line = (cols * 4 + 1) * "-"
    print(line)

    for row in board:
        print("| " + " | ".join(cell if cell else " " for cell in row) + " |")
        print(line)
