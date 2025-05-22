# Tic Tac Toe Game

This is a fully playable 2-player Tic Tac Toe game implemented using OpenGL. The game features a 3x3 grid, mouse click functionality for player moves, win/draw state checking, and a restart game button.

## Project Structure

```
tic-tac-toe
├── src
│   ├── main.py        # Entry point for the game
│   ├── game.py        # Game logic and state management
│   ├── renderer.py     # Rendering the game using OpenGL
│   └── utils.py       # Utility functions for the game
├── requirements.txt   # Required dependencies
└── README.md          # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tic-tac-toe
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python src/main.py
   ```

## How to Play

- The game is played on a 3x3 grid.
- Players take turns clicking on the grid to place their marks (X or O).
- The game checks for a win or draw after each move.
- If a player wins or the game ends in a draw, a restart button will appear to start a new game.

## Additional Features

- Implement AI for single-player mode.
- Add sound effects for moves and game outcomes.
- Enhance the UI with animations and improved graphics.

Feel free to contribute to the project by adding new features or improving existing ones!