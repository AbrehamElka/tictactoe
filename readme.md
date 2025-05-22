# Tic Tac Toe Game using OpenGL

This project implements a fully playable Tic Tac Toe game in Python using OpenGL. It provides two gameplay modes:

- **Two Players Mode:** Two human players take turns on the same device.
- **Against AI Mode:** Play against an AI opponent that uses the minimax algorithm to determine the best moves. When playing against AI, you will choose your mark (X or O). Choosing O lets the AI start the game automatically.

## Features

- **3x3 Grid:** A graphical grid is drawn using OpenGL.
- **Mouse Input:** Left mouse clicks to place marks on the grid.
- **Win/Draw Detection:** The game automatically detects winning and draw situations.
- **Animated Win Line:** If a player wins, an animated line is drawn through the winning cells.
- **Menu System:** Main menu options for Two Players, Against AI, and Close; plus a submenu for choosing your mark in AI mode.
- **Restart & Navigation:** After a game ends, options to play again or return to the main menu are available.

## Project Structure

```
tic-tac-toe
├── src
│   ├── main.py         # Entry point, handles window creation, input, and game state.
│   ├── game.py         # Contains the game logic, board state, win/draw checks.
│   ├── renderer.py     # Renders the grid, marks, menus, and win animation.
│   └── utils.py        # Contains the minimax AI implementation and helper functions.
├── requirements.txt    # Required Python dependencies.
└── README.md           # This file.
```

## How It Works

1. **Initialization:**
   - An instance of [`Game`](tic-tac-toe/src/game.py) is created to manage the board, current player, and game status.
   - The [`Renderer`](tic-tac-toe/src/renderer.py) instance draws the grid, player marks, win line animation, and all menu screens.
   - Global state variables in [`main.py`](tic-tac-toe/src/main.py) keep track of the current mode, menus, and player selections.

2. **Game Modes & Menus:**
   - The **Main Menu** offers three options: *Two Players*, *Against AI*, and *Close*.
   - In **Against AI Mode**, a submenu allows you to choose to play as X or O. The AI takes the opposite mark. If you choose O, the AI makes its move immediately.
   - Mouse inputs convert screen coordinates to board coordinates to handle moves and menu interactions.

3. **Game Logic & AI:**
   - Each move is handled by methods in [`Game`](tic-tac-toe/src/game.py), which checks for winning or draw conditions.
   - On win, a win line is animated using functions in [`Renderer.draw_win_line`](tic-tac-toe/src/renderer.py).
   - The AI uses the minimax algorithm implemented in [`utils.py`](tic-tac-toe/src/utils.py) to decide its moves. The function [`get_best_move`](tic-tac-toe/src/utils.py) evaluates the board and returns the optimal move.

4. **Animation & State Transitions:**
   - GLUT timer functions control delays for win animations and AI moves.
   - The result menu displays either the win/lose outcome or a draw, and provides options to restart or return to the main menu.

## How to Run

### Prerequisites

- Python 3.x
- Install dependencies from [`requirements.txt`](tic-tac-toe/requirements.txt):
  ```sh
  pip install -r requirements.txt
  ```

### Running the Game

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd tic-tac-toe
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Game:**
   ```sh
   python src/main.py
   ```

Enjoy playing Tic Tac Toe!
