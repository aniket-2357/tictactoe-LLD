from collections import deque

from Player import *
from PlayingPieceX import *
from PlayingPieceO import *
from Board import *
class TicTacToeGame:

    def __init__(self):
        self.players = deque()
        self.game_board = None

    def initialize_game(self):
        # Creating 2 players
        cross_piece = PlayingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize board
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True

        while no_winner:
            # Take out the player whose turn it is and also put the player back in the list
            player_turn = self.players.popleft()

            # Get the free spaces from the board
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            # Read the user input
            input_row, input_column = map(int, input(f"Player: {player_turn.name} Enter row, column: ").split(','))

            # Place the piece
            piece_added_successfully = self.game_board.add_piece(input_row, input_column, player_turn.playing_piece)
            if not piece_added_successfully:
                # Player cannot insert the piece into this cell, player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            if self.is_there_winner(input_row, input_column, player_turn.playing_piece.piece_type):
                return player_turn.name

        return "tie"

    def is_there_winner(self, row: int, column: int, piece_type: PieceType) -> bool:
        row_match = all(self.game_board.board[row][i] is not None and self.game_board.board[row][i].piece_type == piece_type for i in range(self.game_board.size))
        column_match = all(self.game_board.board[i][column] is not None and self.game_board.board[i][column].piece_type == piece_type for i in range(self.game_board.size))
        diagonal_match = all(self.game_board.board[i][i] is not None and self.game_board.board[i][i].piece_type == piece_type for i in range(self.game_board.size))
        anti_diagonal_match = all(self.game_board.board[i][self.game_board.size - 1 - i] is not None and self.game_board.board[i][self.game_board.size - 1 - i].piece_type == piece_type for i in range(self.game_board.size))

        return row_match or column_match or diagonal_match or anti_diagonal_match
