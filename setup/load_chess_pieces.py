import os
import pygame


def load_chess_pieces():
    piece_images = {}
    PIECE_FOLDER = "chess_pieces"

    pieces = [
        "white-pawn", "white-rook", "white-knight", "white-bishop", "white-queen", "white-king",
        "black-pawn", "black-rook", "black-knight", "black-bishop", "black-queen", "black-king"    
    ]

    for piece in pieces:
        image_path = os.path.join(PIECE_FOLDER, piece + ".png")
        image = pygame.image.load(image_path)
        resized = pygame.transform.scale(image, (80, 80))
        piece_images[piece] = resized

    return piece_images


