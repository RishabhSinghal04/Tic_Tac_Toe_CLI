from user_input import user_input


def board_size() -> int:
    min_value, max_value = 3, 5
    try:
        n: int = user_input("Select Board (3x3, 4x4, 5x5): ", max_value, min_value)
        return n
    except:
        return -1
