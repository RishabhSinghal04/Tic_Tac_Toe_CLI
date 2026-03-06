from board import create_board, display_board, board_size
from move import move
from user_input import user_input
from .show_menu_options import show_menu_options
from .constants import DEFAULT_BOARD_SIZE, AI_LEVELS, MENU_OPTIONS


def select_ai_level() -> str:
    """
    Display AI difficulty levels and return the selected level.

    Returns:
        str: The chosen AI difficulty level.
    """
    show_menu_options(AI_LEVELS)
    return AI_LEVELS.get(user_input("Enter your choice: ", len(AI_LEVELS)), "1")


def display_ai_symbol_options(symbol_1: str, symbol_2: str) -> None:
    """
    Display AI symbol choices to the user.
    Args:
    symbol_1 (str): First symbol option.
    symbol_2 (str): Second symbol option.

    Note:
        This function only displays options and does not return a value.
    """
    print(f"\nSelect Symbol for AI")
    print(f"Press 1 to use '{symbol_1}'")
    print(f"Press 2 to use '{symbol_2}'")


def select_ai_symbol(symbol_1: str, symbol_2: str) -> str:
    """
    Allow the user to select which symbol the AI will use.

    Args:
        symbol_1 (str): First symbol option.
        symbol_2 (str): Second symbol option.

    Returns:
        str: The chosen symbol for AI.
    """
    display_ai_symbol_options(symbol_1, symbol_2)
    choice: int = user_input("Enter your choice: ", 2)
    return symbol_1 if choice == 1 else symbol_2


def menu() -> None:
    """
    Display the main menu and handle game mode selection.

    Args:
        board: The game board object to be passed into the move function.

    Returns:
        None or result of move(): Depending on user choice.
    """
    n: int = DEFAULT_BOARD_SIZE

    while True:
        show_menu_options(MENU_OPTIONS)
        option: int = user_input("Enter your choice: ", len(MENU_OPTIONS))
        players: dict[str, str] = {"X": "human", "O": "human"}

        if option == 1:
            _play_game(n, players, _start_vs_computer)
        elif option == 2:
            _play_game(n, players, _start_two_players)
        elif option == 3:
            n = board_size()
            if n < 3:
                n = DEFAULT_BOARD_SIZE
        elif option == 4:
            _about()
        elif option == 0:
            return _quit_game()


def _play_game(n: int, players: dict[str, str], game_starter) -> None:
    board: list[list[str]] = create_board(n)
    display_board(board)
    result: str = game_starter(board, players)
    _declare_result(result)


def _start_vs_computer(board: list[list[str]], players: dict[str, str]) -> str:
    ai_difficulty: str = select_ai_level()

    ai_symbol: str = select_ai_symbol("X", "O")
    players[ai_symbol] = "ai"

    print(f"\nAI Difficulty Selected: {ai_difficulty}")
    print(f"AI Symbol Selected: {ai_symbol}\n")

    return move(board, players, ai_difficulty)


def _start_two_players(board: list[list[str]], players: dict[str, str]) -> str:
    print("2 Players Mode\n")
    return move(board, players)


def _quit_game() -> None:
    print("\nGame Exited.\n")


def _declare_result(result: str) -> None:
    print(f"Player {result} Wins!" if result != "" else "Game Draw\n")


def _about() -> None:
    print(f"Player must enter a cell number to place 'X' or 'O'\n")
