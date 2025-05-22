def mouse_to_grid(x, y):
    """Convert mouse click coordinates to grid positions."""
    grid_size = 3
    cell_size = 200  # Assuming each cell is 200x200 pixels
    grid_x = x // cell_size
    grid_y = y // cell_size
    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
        return grid_x, grid_y
    return None

def draw_text(text, x, y):
    """Utility function to draw text on the screen."""
    # This function would use OpenGL to render text at the specified coordinates
    pass

def reset_game_state():
    """Utility function to reset the game state."""
    return [[' ' for _ in range(3)] for _ in range(3)], 'X'  # Returns an empty grid and the starting player

# ---------------- Minimax AI functions ------------------
import copy

def evaluate(board, ai_mark, human_mark):
    # Check rows, columns, and diagonals for a win.
    lines = [
        # rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # columns
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for line in lines:
        a,b,c = line
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != ' ':
            if board[a[0]][a[1]] == ai_mark:
                return 10
            elif board[a[0]][a[1]] == human_mark:
                return -10
    return 0

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def minimax(board, depth, is_maximizing, ai_mark, human_mark):
    score = evaluate(board, ai_mark, human_mark)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai_mark
                    best = max(best, minimax(board, depth+1, False, ai_mark, human_mark))
                    board[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = human_mark
                    best = min(best, minimax(board, depth+1, True, ai_mark, human_mark))
                    board[i][j] = ' '
        return best

def get_best_move(board, ai_mark, human_mark):
    best_val = -1000
    best_move = None
    new_board = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if new_board[i][j] == ' ':
                new_board[i][j] = ai_mark
                move_val = minimax(new_board, 0, False, ai_mark, human_mark)
                new_board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move