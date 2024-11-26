from PieceType import *
class PlayingPiece:
    def __init__(self, piece_type):
        if not isinstance(piece_type, PieceType):
            raise ValueError("Invalid piece type")
        self.piece_type = piece_type
