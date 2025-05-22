# renderer.py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time

def draw_text(text, x, y):
    glColor3f(1, 1, 0)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

class Renderer:
    def __init__(self, game):
        self.game = game
        self.win_line_progress = 0.0  # from 0.0 to 1.0
        self.win_line_start_time = None

    def draw_grid(self):
        glColor3f(1, 1, 1)
        glBegin(GL_LINES)
        for i in range(1, 3):
            glVertex2f(i, 0)
            glVertex2f(i, 3)
            glVertex2f(0, i)
            glVertex2f(3, i)
        glEnd()

    def draw_marks(self):
        for row in range(3):
            for col in range(3):
                mark = self.game.board[row][col]
                if mark != ' ':
                    cx = col + 0.5
                    cy = row + 0.5
                    self.draw_mark(mark, cx, cy)

    def draw_mark(self, mark, x, y):
        if mark == 'X':
            glColor3f(1, 0, 0)
            glBegin(GL_LINES)
            glVertex2f(x - 0.3, y - 0.3)
            glVertex2f(x + 0.3, y + 0.3)
            glVertex2f(x - 0.3, y + 0.3)
            glVertex2f(x + 0.3, y - 0.3)
            glEnd()
        elif mark == 'O':
            glColor3f(0, 0, 1)
            num_segments = 50
            glBegin(GL_LINE_LOOP)
            for i in range(num_segments):
                theta = 2.0 * np.pi * i / num_segments
                dx = 0.3 * np.cos(theta)
                dy = 0.3 * np.sin(theta)
                glVertex2f(x + dx, y + dy)
            glEnd()
    
    def draw_win_line(self):
        if not self.game.winning_line or len(self.game.winning_line) < 2:
            return

        if self.win_line_start_time is None:
            self.win_line_start_time = time.time()

        # Animate for 1 second (as set in main.py glutTimerFunc)
        elapsed = time.time() - self.win_line_start_time
        duration = 1 # Match this with the glutTimerFunc delay
        progress = min(elapsed / duration, 1.0)
        self.win_line_progress = progress

        start = self.game.winning_line[0]
        end = self.game.winning_line[1]

        def cell_center(cell):
            return (cell[1] + 0.5, cell[0] + 0.5)

        start_coords = cell_center(start)
        end_coords = cell_center(end)

        current_x = start_coords[0] + (end_coords[0] - start_coords[0]) * self.win_line_progress
        current_y = start_coords[1] + (end_coords[1] - start_coords[1]) * self.win_line_progress

        glColor3f(1.0, 1.0, 0.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)
        glVertex2f(*start_coords)
        glVertex2f(current_x, current_y)
        glEnd()

    def render(self):
        self.draw_grid()
        self.draw_marks()
        if self.game.game_over:
            self.draw_win_line()

    def draw_menu(self):
        # Draw background
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(3, 0)
        glVertex2f(3, 3)
        glVertex2f(0, 3)
        glEnd()

        # Title
        glColor3f(1, 1, 1)
        draw_text("TIC TAC TOE", 1.0, 2.6)

        # Two Players Button: (1.0,2.2)-(2.0,2.5)
        glColor3f(0.2, 0.7, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 2.2)
        glVertex2f(2.0, 2.2)
        glVertex2f(2.0, 2.5)
        glVertex2f(1.0, 2.5)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Two Players", 1.1, 2.35)

        # Against AI Button: (1.0,1.6)-(2.0,1.9)
        glColor3f(0.2, 0.7, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 1.6)
        glVertex2f(2.0, 1.6)
        glVertex2f(2.0, 1.9)
        glVertex2f(1.0, 1.9)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Against AI", 1.2, 1.75)

        # Close Button: (1.0,1.0)-(2.0,1.3)
        glColor3f(0.8, 0.2, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 1.0)
        glVertex2f(2.0, 1.0)
        glVertex2f(2.0, 1.3)
        glVertex2f(1.0, 1.3)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Close", 1.3, 1.12)

    def draw_ai_choice(self):
        # Draw background
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(3, 0)
        glVertex2f(3, 3)
        glVertex2f(0, 3)
        glEnd()

        # Title
        glColor3f(1, 1, 1)
        draw_text("Choose Your Side", 0.8, 2.6)

        # Play as X Button: (1.0,2.0)-(2.0,2.3)
        glColor3f(0.2, 0.7, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 2.0)
        glVertex2f(2.0, 2.0)
        glVertex2f(2.0, 2.3)
        glVertex2f(1.0, 2.3)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Play as X", 1.1, 2.15)

        # Play as O Button: (1.0,1.4)-(2.0,1.7)
        glColor3f(0.2, 0.7, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 1.4)
        glVertex2f(2.0, 1.4)
        glVertex2f(2.0, 1.7)
        glVertex2f(1.0, 1.7)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Play as O", 1.2, 1.55)

        # Exit Button: (1.0,0.8)-(2.0,1.1)
        glColor3f(0.8, 0.2, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 0.8)
        glVertex2f(2.0, 0.8)
        glVertex2f(2.0, 1.1)
        glVertex2f(1.0, 1.1)
        glEnd()
        glColor3f(0, 0, 0)
        draw_text("Exit", 1.3, 0.9)

    def draw_win_screen(self):
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(3, 0)
        glVertex2f(3, 3)
        glVertex2f(0, 3)
        glEnd()

        # Winner text
        glColor3f(1, 1, 1)
        glRasterPos2f(1.0, 2.2)
        message = f"{self.game.winner} Wins!" if self.game.winner else "It's a Draw!"
        for char in message:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        # "Play Again" Button: (1.0,1.5)-(2.0,1.8) - Adjusted Y-coordinate
        glColor3f(0.2, 0.8, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 1.5)
        glVertex2f(2.0, 1.5)
        glVertex2f(2.0, 1.8)
        glVertex2f(1.0, 1.8)
        glEnd()
        glColor3f(0, 0, 0)
        glRasterPos2f(1.15, 1.65)
        for ch in "Play Again":
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

        # "Main Menu" Button: (1.0,1.0)-(2.0,1.3) - New button
        glColor3f(0.2, 0.5, 0.8) # Blueish color for Main Menu
        glBegin(GL_QUADS)
        glVertex2f(1.0, 1.0)
        glVertex2f(2.0, 1.0)
        glVertex2f(2.0, 1.3)
        glVertex2f(1.0, 1.3)
        glEnd()
        glColor3f(0, 0, 0)
        glRasterPos2f(1.15, 1.15)
        for ch in "Main Menu":
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

        # "Close" Button: (1.0,0.5)-(2.0,0.8) - Adjusted Y-coordinate
        glColor3f(0.8, 0.2, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(1.0, 0.5)
        glVertex2f(2.0, 0.5)
        glVertex2f(2.0, 0.8)
        glVertex2f(1.0, 0.8)
        glEnd()
        glColor3f(0, 0, 0)
        glRasterPos2f(1.3, 0.65)
        for ch in "Close":
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))