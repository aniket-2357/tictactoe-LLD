class Player:
    def __init__(self, name, playing_piece):
        self._name = name
        self._playing_piece = playing_piece

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def playing_piece(self):
        return self._playing_piece

    @playing_piece.setter
    def playing_piece(self, playing_piece):
        self._playing_piece = playing_piece
