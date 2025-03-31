import pygame
import sys
from setup.load_chess_pieces import load_chess_pieces
from logic.board_state import get_starting_board
from logic.check_square import check_square

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640  # Window size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors (RGB)
WHITE = (240, 217, 181)   # Light square
BROWN = (181, 136, 99)    # Dark square

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trixies Awesome Chess Board")

piece_images = load_chess_pieces()
board = get_starting_board()

# Function to draw the board
def draw_board(win):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



def main():
    selected_square = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                selected_square = check_square(event, SQUARE_SIZE, board, selected_square)

        # DRAW EVERYTHING ON SCREEN HERE:

        draw_board(win)  # draw background

        # ✅ Draw selected square highlight AFTER drawing the board
        if selected_square:
            highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
            highlight_surface.set_alpha(100)
            highlight_surface.fill((0, 255, 0))
            r, c = selected_square
            win.blit(highlight_surface, (c * SQUARE_SIZE, r * SQUARE_SIZE))

        # draw pieces
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece:
                    win.blit(piece_images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

        pygame.display.flip()


if __name__ == "__main__":
    main()
