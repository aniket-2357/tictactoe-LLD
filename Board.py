


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row, column, playing_piece):
        if row < 0 or column < 0 or row >= self.size or column >= self.size:
            raise ValueError("Row and column must be within board boundaries.")
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))
        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(self.board[i][j].piece_type, end="   ")
                else:
                    print("    ", end="")
                if j < self.size - 1:
                    print("|", end="")
            print()
            if i < self.size - 1:
                print("----" * self.size)