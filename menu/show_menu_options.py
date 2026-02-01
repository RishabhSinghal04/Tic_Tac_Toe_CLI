def show_menu_options(options : dict) -> None:
    """
    Display menu options in a clean, numbered format.

    Args:
        options (dict): A dictionary where keys are option numbers (int)
                        and values are option descriptions (str).
    """
    for key, value in options.items():
        print(f"{key}. {value}")