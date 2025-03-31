import pygame
import sys

def check_square(event, SQUARE_SIZE, board, selected_square):
    mouse_x, mouse_y = event.pos  # ← proper click position
    col = mouse_x // SQUARE_SIZE
    row = mouse_y // SQUARE_SIZE

    if selected_square:
        start_row, start_col = selected_square

        if (start_row, start_col) == (row, col):
            print("Deselected.")
            selected_square = None
        else:
            piece = board[start_row][start_col]
            board[row][col] = piece
            board[start_row][start_col] = None
            print(f"Moved {piece} from ({start_row}, {start_col}) to ({row}, {col})")
            selected_square = None
    else:
        if board[row][col]:
            selected_square = (row, col)
            print(f"Selected {board[row][col]} at ({row}, {col})")
          
    return selected_square