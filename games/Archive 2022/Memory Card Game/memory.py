
import pygame, random, sys, time
from card import Card
from pygame.locals import *


#---------- Main Constants ----------#
FPS          = 60
WINDOW_X     = 640
WINDOW_Y     = 480
BOARD_X      = 8
BOARD_Y      = 4
CELLSIZE     = 60
CELL_MARGIN  = 10
X_MARGIN = int((WINDOW_X - (BOARD_X * (CELLSIZE + CELL_MARGIN))) / 2)
Y_MARGIN = int((WINDOW_Y - (BOARD_Y * (CELLSIZE + CELL_MARGIN))) / 2)

DONUT   = 'donut'
SQUARE  = 'square'
DIAMOND = 'diamond'
CIRCLE  = 'oval'


#---------- Colors ----------#
BACKGROUND  = (24, 20, 153)
BOARD       = (61, 15, 212)
BOARDSHADOW = ( 41, 128, 185)
HIDDEN      = ( 75, 119, 190)
CARDSHADOW  = ( 44,  62,  80)  
HIGHLIGHT   = (236, 240, 241) 

COLOR_1    = ( 39, 174,  96)
TINT_1     = ( 46, 204, 113)
COLOR_2    = (241, 196,  15)
TINT_2     = (243, 156,  18)
COLOR_3    = ( 52, 152, 219)
TINT_3     = ( 41, 128, 185)
COLOR_4    = (231,  76,  60)
TINT_4     = (192,  57,  43)


#---------- List Constants ----------#
SHAPE_LIST = (DONUT, SQUARE, DIAMOND, CIRCLE)
COLOR_LIST = (COLOR_1, COLOR_2, COLOR_3, COLOR_4)


#---------- Pygame init ----------#
pygame.init()
DISPLAY = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
DISPLAY.convert_alpha()
pygame.display.set_caption('Memory')


class Game:
    """Main game class."""
    
    def create_icon_list(self):
        """Create randomized list of icons and colors for card placement."""
        icon_list = []
        for color in COLOR_LIST:
            for shape in SHAPE_LIST:
                icon_list.append((shape, color))

        icon_list *= 2
        random.shuffle(icon_list)
        return icon_list


    def create_board(self, icons):
        """Create board grid, draw board graphics, create card objects."""
        board = []
        for x in range(BOARD_X):
            column = []
            for y in range(BOARD_Y):
                card = Card(x, y, icons)
                column.append(card)
                del icons[0]
            board.append(column)
        pygame.draw.rect(DISPLAY, BOARDSHADOW, [
            X_MARGIN / 2, 
            Y_MARGIN / 2, 
            WINDOW_X - X_MARGIN, 
            WINDOW_Y - Y_MARGIN + 4
            ])
        pygame.draw.rect(DISPLAY, BOARD, [
            X_MARGIN / 2, 
            Y_MARGIN / 2, 
            WINDOW_X - X_MARGIN, 
            WINDOW_Y - Y_MARGIN
            ])
        return board


    def update_board(self, board):
        """Redraw card graphics with frame updates/user selection."""
        for card in Card.instances:
            if card.mode == 0:
                self.draw_card(card, HIDDEN)
            elif card.mode == 1:
                self.draw_card(card, HIGHLIGHT)
            elif card.mode == 2:
                self.draw_card(card, card.color)
                self.draw_card_icon(card)


    def draw_card(self, card, color):
        """Draw base card graphics."""
        pygame.draw.rect(DISPLAY, CARDSHADOW, [
            (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
            (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2) + CELLSIZE - 1, 
            CELLSIZE, 4
            ])
        card.rect = pygame.draw.rect(DISPLAY, color, [
            (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
            (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
            CELLSIZE, CELLSIZE
            ])


    def left_top_coords(self, card):
        """Determine upper left rectangle coordinates of card for draw functions."""
        left = int((CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2))
        top = int((CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2))
        return (left, top)


    def draw_card_icon(self, card):
        """Draw card color and icon."""
        if card.color == COLOR_1:
            tint = TINT_1
        elif card.color == COLOR_2:
            tint = TINT_2
        elif card.color == COLOR_3:
            tint = TINT_3
        elif card.color == COLOR_4:
            tint = TINT_4
        half = int(CELLSIZE * 0.5)
        quarter = int(CELLSIZE * 0.25)
        left, top = self.left_top_coords(card)
        if card.icon == DONUT:
            pygame.draw.circle(DISPLAY, tint, 
                (left + half, top + half), half - 10)
            pygame.draw.circle(DISPLAY, card.color, 
                (left + half, top + half), quarter - 2)
        elif card.icon == SQUARE:
            pygame.draw.rect(DISPLAY, tint, 
                (left + quarter, top + quarter, CELLSIZE - half, CELLSIZE - half))
        elif card.icon == DIAMOND:
            pygame.draw.polygon(DISPLAY, tint, (
                (left + half, top + 6), 
                (left + CELLSIZE - 10, top + half + 4), 
                (left + half, top + CELLSIZE - 8), 
                (left + 10, top + half + 4)
                ))
        elif card.icon == CIRCLE:
            pygame.draw.circle(DISPLAY, tint, (left + half, top + half), half - 10)


    def hide_card(self, card, clock):
        """Card hide animation for game beginning and incorrect guesses."""
        for coverage in range(0, 60, 6):
            pygame.draw.rect(DISPLAY, HIDDEN, [
                (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                CELLSIZE, coverage + 6
                ])
            pygame.display.flip()
            clock.tick(FPS)
        card.mode = 0


    def show_card(self, card, clock):
        """Card flip animation on user selection."""
        for coverage in range(0, 60, 6):
            pygame.draw.rect(DISPLAY, card.color, [
                (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                CELLSIZE, CELLSIZE
                ])
            pygame.draw.rect(DISPLAY, HIDDEN, [
                (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                CELLSIZE, 60 - coverage
                ])
            pygame.display.flip()
            clock.tick(FPS)
        Card.guesses.append(card)
        card.mode = 2


    def update_text(self):
        """Redraw font object as guesses correctly guessed."""
        remaining = str(round((len(Card.instances) - len(Card.correct)) / 2))
        fontObj = pygame.font.Font('OpenSans-Light.ttf', 24)
        textObj = fontObj.render('Remaining: ' + remaining, True, HIGHLIGHT, BACKGROUND)
        textRect = textObj.get_rect()
        textRect.center = ((WINDOW_X / 2), 24)
        DISPLAY.fill(BACKGROUND, (0, 0, WINDOW_X, 50))
        DISPLAY.blit(textObj, textRect)

    
    def check_guess(self, clock):
        """Check for win event when two guesses selected."""
        pygame.time.wait(500)
        first, second = Card.guesses[0], Card.guesses[1]
        if first.color == second.color and first.icon == second.icon:
            Card.correct.append(first)
            Card.correct.append(second)
            del Card.guesses[:]
        else:
            for card in Card.guesses:
                self.hide_card(card, clock)
            del Card.guesses[:]





def main():
    clock = pygame.time.Clock()

    # Board creation
    creating_board = True
    while creating_board:
        DISPLAY.fill(BACKGROUND)
        game = Game()
        icons = game.create_icon_list()
        board = game.create_board(icons)
        game.update_board(board)
        game.update_text()
        creating_board = False

    # Card begin animation
    random.shuffle(Card.instances)
    for card in Card.instances:
        game.hide_card(card, clock)

    # Main game loop
    guesses = 0
    running = True
    startTime = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for card in Card.instances:
                    if card.mode != 2:
                        if card.rect.collidepoint(mouse_x, mouse_y):
                            card.mode = 1
                        else:
                            card.mode = 0

            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if guesses < 2:
                    for card in Card.instances:
                        if card.rect.collidepoint(mouse_x, mouse_y) and card not in Card.correct and card not in Card.guesses:
                            guesses += 1
                            game.show_card(card, clock)

        game.update_board(board)
        game.update_text()
        pygame.display.flip()
        clock.tick(FPS)

        # If two guesses made by end of frame, check for match
        if guesses == 2:
            game.check_guess(clock)
            guesses = 0

        # If all cards present in 'correct' instances, game over
        if len(Card.correct) == len(Card.instances):
            timeTotal = str(round(time.time() - startTime, 2))
            win = DISPLAY.convert_alpha()
            for alpha in range(0, 30):
                pygame.draw.rect(win, (236, 240, 241, alpha), [0, 0, WINDOW_X, WINDOW_Y])
                DISPLAY.blit(win, (0, 0))
                pygame.display.flip()
                clock.tick(FPS)

            fontObj = pygame.font.Font('OpenSans-Regular.ttf', 36)
            textObj = fontObj.render('Completed in ' + timeTotal + 's', False, BACKGROUND)
            textRect = textObj.get_rect()
            textRect.center = ((WINDOW_X / 2), (WINDOW_Y / 2))
            DISPLAY.blit(textObj, textRect)

            pygame.display.flip()
            clock.tick(FPS)
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()




if __name__ == "__main__":
    main()