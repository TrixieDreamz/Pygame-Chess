import pygame
import sys

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
pygame.display.set_caption("Empty Chess Board")

# Function to draw the board
def draw_board(win):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(win)
        pygame.display.flip()

if __name__ == "__main__":
    main()
