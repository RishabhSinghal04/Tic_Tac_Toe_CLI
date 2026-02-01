from board import create_board, display_board, total_cells
from menu import menu

def main():
    # 'N' Rows, 'N' Columns
    N = 3
    board = create_board(N)
    num_of_cells = total_cells(board)

    display_board(board)
    print(
        f"Player must enter a cell number from 1 to {num_of_cells} to place 'X' or 'O'\n"
    )

    result = menu(board)
    if result is None:
        print("Game Exited")
        return
    print(f"Player {result} Wins!" if result != "" else "Game Draw")


if __name__ == "__main__":
    main()
