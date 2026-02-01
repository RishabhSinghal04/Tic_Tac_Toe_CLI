from move import move
from user_input import user_input
from .constants import AI_LEVELS, MENU_OPTIONS
from .show_menu_options import show_menu_options


def select_ai_level() -> str:
    """
    Display AI difficulty levels and return the selected level.

    Returns:
        str: The chosen AI difficulty level.
    """
    show_menu_options(AI_LEVELS)
    return AI_LEVELS.get(user_input("Enter your choice: ", len(AI_LEVELS)))


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
    choice = user_input("Enter your choice: ", 2)
    return symbol_1 if choice == 1 else symbol_2


def menu(board):
    """
    Display the main menu and handle game mode selection.

    Args:
        board: The game board object to be passed into the move function.

    Returns:
        None or result of move(): Depending on user choice.
    """
    players = {"X": "human", "O": "human"}

    show_menu_options(MENU_OPTIONS)
    option = user_input("Enter your choice: ", len(MENU_OPTIONS))

    if option == 1:
        return _start_vs_computer(board, players)
    elif option == 2:
        return _start_two_players(board, players)
    elif option == 3:
        return _quit_game()


def _start_vs_computer(board, players: dict) -> str:
    ai_difficulty = select_ai_level()

    ai_symbol = select_ai_symbol("X", "O")
    players[ai_symbol] = "ai"

    print(f"\nAI Difficulty Selected: {ai_difficulty}")
    print(f"AI Symbol Selected: {ai_symbol}\n")

    return move(board, players, ai_difficulty)


def _start_two_players(board, players: dict) -> str:
    print("\n2 Players Mode\n")
    return move(board, players)


def _quit_game() -> None:
    print("\nQuitting the game.\n")
