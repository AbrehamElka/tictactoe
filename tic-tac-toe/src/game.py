class Game:
    def __init__(self):
        self.reset_game()
        self.winning_line = None

    def make_move(self, row, col):
        if self.board[row][col] == ' ' and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_winner():
                # Winning state already set by check_winner
                self.winner = self.current_player
            elif self.check_draw():
                self.game_over = True
                self.winner = None  # Draw
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        lines = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for line in lines:
            a, b, c = line
            if self.board[a[0]][a[1]] != ' ' and self.board[a[0]][a[1]] == self.board[b[0]][b[1]] == self.board[c[0]][c[1]]:
                self.winner = self.board[a[0]][a[1]]
                self.game_over = True
                self.winning_line = (a, c)
                return True
        return False

    def check_draw(self):
        # Draw state: board full and no winner
        return all(cell != ' ' for row in self.board for cell in row) and self.winner is None

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None  # Must be initialized
        self.winning_line = None
