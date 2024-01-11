import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TRANS = (1, 2, 3)

# CONSTANTS:
WIDTH = 700
HEIGHT = 700
MARK_SIZE = 50


class Game:
    """class to keep track of the status of the game."""

    def __init__(self):
        """
        Start a new game with an empty board and random player going first.
        """
        self.status = 'playing'
        self.turn = random.randrange(2)
        self.players = ['x', 'o']
        self.selected_token = None
        self.jumping = False
        pygame.display.set_caption("%s's turn" % self.players[self.turn % 2])
        self.game_board = [['x', '-', 'x', '-', 'x', '-', 'x', '-'],
                           ['-', 'x', '-', 'x', '-', 'x', '-', 'x'],
                           ['x', '-', 'x', '-', 'x', '-', 'x', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', 'o', '-', 'o', '-', 'o', '-', 'o'],
                           ['o', '-', 'o', '-', 'o', '-', 'o', '-'],
                           ['-', 'o', '-', 'o', '-', 'o', '-', 'o']]

    def evaluate_click(self, mouse_pos):
        """
        Select a token if none is selected.
        Move token to a square if it is a valid move.
        Start a new game if the game is over.
        """
        if self.status == 'playing':
            row, column = get_clicked_row(mouse_pos), get_clicked_column(mouse_pos)
            if self.selected_token:
                move = self.is_valid_move(self.players[self.turn % 2], self.selected_token, row, column)
                if move[0]:
                    self.play(self.players[self.turn % 2], self.selected_token, row, column, move[1])
                elif row == self.selected_token[0] and column == self.selected_token[1]:
                    self.selected_token = None
                    if self.jumping:
                        self.jumping = False
                        self.next_turn()
                else:
                    print
                    'invalid move'
            else:
                if self.game_board[row][column].lower() == self.players[self.turn % 2]:
                    self.selected_token = [row, column]
        elif self.status == 'game over':
            self.__init__()

    def is_valid_move(self, player, token_location, to_row, to_col):
        """
        Check if clicked location is a valid square for player to move to.
        """
        from_row = token_location[0]
        from_col = token_location[1]
        token_char = self.game_board[from_row][from_col]
        if self.game_board[to_row][to_col] != '-':
            return False, None
        if (((token_char.isupper() and abs(from_row - to_row) == 1) or (player == 'x' and to_row - from_row == 1) or
             (player == 'o' and from_row - to_row == 1)) and abs(from_col - to_col) == 1) and not self.jumping:
            return True, None
        if (((token_char.isupper() and abs(from_row - to_row) == 2) or (player == 'x' and to_row - from_row == 2) or
             (player == 'o' and from_row - to_row == 2)) and abs(from_col - to_col) == 2):
            jump_row = (to_row - from_row) / 2 + from_row
            jump_col = (to_col - from_col) / 2 + from_col
            if self.game_board[jump_row][jump_col].lower() not in [player, '-']:
                return True, [jump_row, jump_col]
        return False, None

    def play(self, player, token_location, to_row, to_col, jump):
        """
        Move selected token to a particular square, then check to see if the game is over.
        """
        from_row = token_location[0]
        from_col = token_location[1]
        token_char = self.game_board[from_row][from_col]
        self.game_board[to_row][to_col] = token_char
        self.game_board[from_row][from_col] = '-'
        if (player == 'x' and to_row == 7) or (player == 'o' and to_row == 0):
            self.game_board[to_row][to_col] = token_char.upper()
        if jump:
            self.game_board[jump[0]][jump[1]] = '-'
            self.selected_token = [to_row, to_col]
            self.jumping = True
        else:
            self.selected_token = None
            self.next_turn()
        winner = self.check_winner()
        if winner is None:
            pygame.display.set_caption("%s's turn" % self.players[self.turn % 2])
        elif winner == 'draw':
            pygame.display.set_caption("It's a stalemate! Click to start again")
            self.status = 'game over'
        else:
            pygame.display.set_caption("%s wins! Click to start again" % winner)
            self.status = 'game over'

    def next_turn(self):
        self.turn += 1
        pygame.display.set_caption("%s's turn" % self.players[self.turn % 2])

    def check_winner(self):
        """
        check to see if someone won, or if it is a draw.
        """
        x = sum([row.count('x') + row.count('X') for row in self.game_board])
        if x == 0:
            return 'o'
        o = sum([row.count('o') + row.count('O') for row in self.game_board])
        if o == 0:
            return 'x'
        if x == 1 and o == 1:
            return 'draw'
        return None

    def draw(self):
        """
        Draw the game board and the X's and O's.
        """
        for i in range(9):
            pygame.draw.line(screen, WHITE, [i * WIDTH / 8, 0], [i * WIDTH / 8, HEIGHT], 5)
            pygame.draw.line(screen, WHITE, [0, i * HEIGHT / 8], [WIDTH, i * HEIGHT / 8], 5)
        font = pygame.font.SysFont('Calibri', MARK_SIZE, False, False)
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                mark = self.game_board[r][c]
                if self.players[self.turn % 2] == mark.lower():
                    color = YELLOW
                else:
                    color = WHITE
                if self.selected_token:
                    if self.selected_token[0] == r and self.selected_token[1] == c:
                        color = RED
                if mark != '-':
                    mark_text = font.render(self.game_board[r][c], True, color)
                    x = WIDTH / 8 * c + WIDTH / 16
                    y = HEIGHT / 8 * r + HEIGHT / 16
                    screen.blit(mark_text, [x - mark_text.get_width() / 2, y - mark_text.get_height() / 2])


# Helper functions:
def get_clicked_column(mouse_pos):
    x = mouse_pos[0]
    for i in range(1, 8):
        if x < i * WIDTH / 8:
            return i - 1
    return 7


def get_clicked_row(mouse_pos):
    y = mouse_pos[1]
    for i in range(1, 8):
        if y < i * HEIGHT / 8:
            return i - 1
    return 7


# start pygame:
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# start tic-tac-toe game:
game = Game()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# game loop:
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            entry = str(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            game.evaluate_click(pygame.mouse.get_pos())

    # --- Drawing code should go here

    # First, clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # draw the game board and marks:
    game.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()