# Tic-Tac-Toe with Minimax Algorithm

## Overview

This Tic-Tac-Toe game is implemented in Python and features an AI opponent that uses the Minimax algorithm for decision-making. The project is structured into several modules, including player, board, and game management, and it can be compiled into an executable using PyInstaller for easy distribution.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Play Tic-Tac-Toe against an AI opponent.
- The AI uses the Minimax algorithm to calculate optimal moves.
- Offers a simple and intuitive command-line interface for interaction.

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

## Usage

To run the game, execute the following command:

```bash
python game.py
```

The game will start, and you can play against the AI opponent by entering the row and column numbers corresponding to your move.

## Project Structure

The project structure is organized as follows:

- `player.py`: Contains the Player class, which represents a player in the game.
- `board.py`: Contains the Board class, which represents the game board.
- `game.py`: Contains the Game class, which manages the game flow.
- `minimax.py`: Contains the Minimax class, which implements the Minimax algorithm for the AI opponent.
- `main.py`: Contains the main entry point of the program.

Each module is responsible for a specific aspect of the game and can be easily modified or extended.

```
tic-tac-toe/
├── README.md
├── player.py
├── board.py
├── game.py
├── minimax.py
├── requirements.txt
├── setup.py
└── dist/
    └── tictactoe.exe
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

```




```
