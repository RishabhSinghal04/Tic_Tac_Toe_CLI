def user_input(
    prompt: str, max_value: int, min_value: int = 0, input_func=input
) -> int:
    """
    Prompt the user to enter a valid integer between 1 to max_value (both inclusive).

    Args:
        prompt (str): Message to show to user.
        max_value (int): Maximum valid value.
        min_value (int): Minimum valid value (default: 1).
        input_func (callable): Function to capture user input (default: built-in input).

    Returns:
        int: The valid integer between 1 to max_value (both inclusive).
    """
    if min_value > max_value:
        raise ValueError(
            f"Expected {min_value} <= {max_value}, found {min_value} > {max_value}"
        )
    while True:
        user_value = _get_user_input(prompt, input_func)
        if user_value is not None and _is_valid_input(user_value, min_value, max_value):
            return user_value
        _print_invalid_input_message(min_value, max_value)


def _get_user_input(prompt: str, input_func):
    """
    Capture and convert user input to an integer, handling errors.

    Args:
        prompt (str): Message to show to user.
        input_func (callable): Function to capture user input.

    Returns:
        int: User's input integer, or -1 if input is invalid.
    """
    try:
        return int(input_func(f"{prompt}: "))
    except ValueError:
        return None


def _is_valid_input(user_value: int, min_value: int, max_value: int) -> bool:
    """
    Check if the choice is within the valid range.

    Args:
        user_value (int): User's input integer.
        max_value (int): Maximum valid value.

    Returns:
        bool: True if valid, False otherwise.
    """
    return min_value <= user_value <= max_value


def _print_invalid_input_message(min_value: int, max_value: int) -> None:
    """
    Display an error message for invalid input.

    Args:
        max_value (int): Maximum valid value.
    """
    print(
        f"Invalid Input! Please enter a number between {min_value} and {max_value} (both inclusive)."
    )
