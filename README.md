# Tic Tac Toe CLI

A command-line Tic Tac Toe game featuring both two-player mode and an AI opponent. Designed for simple yet engaging gameplay, this project demonstrates clean Python programming practices and modular design.


## Features

- **Two-player mode**: Play against another human in the same terminal.
- **AI opponent**: Challenge a computer-controlled player with basic decision-making.
- **Command-line interface**: Lightweight and easy to run without external dependencies.
- **Modular codebase**: Organized into separate modules for board, player, moves, and input handling.


## Project Structure

```
Tic_Tac_Toe_CLI/
│
├── board/          # Handles board creation and display
├── menu/           # Game menu and navigation
├── player/         # Player classes (human and AI)
├── __pycache__/    # Compiled Python files
│
├── main.py         # Entry point for the game
├── move.py         # Logic for moves and win conditions
├── user_input.py   # Input handling for players
├── README.md       # Project documentation
└── .gitattributes  # Git attributes configuration
```


## Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RishabhSinghal04/Tic_Tac_Toe_CLI.git
   cd Tic_Tac_Toe_CLI
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```


## Usage

- Launch the game by running `main.py`.
- Choose between:
  - **Two-player mode**: Both players take turns entering their moves.
  - **AI mode**: Play against the computer.
- Input moves by specifying the position on the board (details provided in-game).


## Development Environment

- **Language**: Python 3.13
- **Editor**: Visual Studio Code
- **Environment**: Command-line interface
- **Design**: Modular structure for scalability and readability


## Contributing

Contributions are welcome!