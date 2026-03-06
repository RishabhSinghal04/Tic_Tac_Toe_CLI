from board import check_winner


def minimax(
    board: list[list[str]],
    depth: int,
    is_maximizing: bool,
    ai_player: str,
    human_player: str,
    alpha: float = -float("inf"),
    beta: float = float("inf"),
):
    if check_winner(board, ai_player):
        return 10 - depth
    if check_winner(board, human_player):
        return depth - 10
    if all(cell != "" for row in board for cell in row):
        return 0

    n: int = len(board)
    num_of_cells: int = n * n

    if is_maximizing:
        max_eval: float = -float("inf")
        for position in range(1, num_of_cells + 1):
            row, col = divmod(position - 1, n)
            if board[row][col] == "":
                board[row][col] = ai_player
                eval_score = minimax(board, depth + 1, False, ai_player, human_player)
                board[row][col] = ""
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for position in range(1, num_of_cells + 1):
            row, col = divmod(position - 1, n)
            if board[row][col] == "":
                board[row][col] = human_player
                eval_score = minimax(board, depth + 1, True, ai_player, human_player)
                board[row][col] = ""
                min_eval: float = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval
