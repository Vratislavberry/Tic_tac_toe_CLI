import os
from copy import deepcopy
from termcolor import colored

class Tic_tac_toe:
    def __init__(self):
        self.board_size = 20
        self.board = self._create_board()
        self.player_on_turn = "X"
        self.winner = ""
        self.win_symbols = []

    def _create_board(self):
        board = []
        for _ in range(self.board_size):
            row = ["·" for _ in range(self.board_size)]
            board.append(row)
        return board

    def update_board(self):
        os.system("cls")
        # printing of upper heading
        print("   ", end="")
        for num in range(self.board_size):
            print(chr(num+65), end="  ")
        print()

        # printing of the board
        for vertikalni_index, row in enumerate(self.board):
            vertikalni_index += 1 # Pro vypisovani od 1-20 mist 0-19
            # side-panel heading
            if vertikalni_index < 10:
                print(vertikalni_index, end="  ")
            else:
                print(vertikalni_index, end=" ")
            # Individual cells
            if len(self.win_symbols) == 0:
                for field in row:
                    print(field, end="  ")
                print()
            else:
                for horizontalni_index, field in enumerate(row):
                    if (vertikalni_index-1, horizontalni_index) in self.win_symbols:
                        print(colored(field, "green"), end="  ")
                    else:
                        print(field, end="  ")
                print()

    def switch_player(self):
        self.player_on_turn = "X" if self.player_on_turn != "X" else "O"  # zmena hrace na konci kola

    def get_coordinates(self):
        while True:

            user_input = input("Enter coordinates (e.g. A1): ")
            x = (ord(user_input[0].upper())-65)
            y = 0
            print()
            try:
                y = int(user_input[1:])-1
            except ValueError:
                print(colored("Enter valid coordinates.", "red"))
                continue

            if 0 <= x <= self.board_size-1 and 0 <= y <= self.board_size-1 and self.board[y][x] == "·":
                break
            print(colored("Enter valid coordinates.", "red"))
        return x, y

    def make_turn(self, x, y):
        self.board[y][x] = self.player_on_turn

    def _horizontal_win(self):
        copied_board = deepcopy(self.board)
        for i, row in enumerate(copied_board):
            for _ in range(row.count(self.player_on_turn)):
                symbol_index = row.index(self.player_on_turn)
                row[row.index(self.player_on_turn)] = "End"
                if symbol_index >= 2 and symbol_index <= self.board_size-3:
                    if row[symbol_index-2] in [self.player_on_turn, "End"] and row[symbol_index-1] in [self.player_on_turn, "End"]:
                        if row[symbol_index+1] in [self.player_on_turn, "End"] and row[symbol_index+2] in [self.player_on_turn, "End"]:
                            for a in range(-2, 3):
                                self.win_symbols.append((i, symbol_index+a))
                            return 1

    def _vertical_win(self):
        copied_board = deepcopy(self.board)
        for i, row in enumerate(copied_board[2:18]):
            i += 2
            for _ in range(row.count(self.player_on_turn)):
                symbol_index = row.index(self.player_on_turn)
                row[row.index(self.player_on_turn)] = "End"
                if copied_board[i-2][symbol_index] in [self.player_on_turn, "End"] and copied_board[i-1][symbol_index] in [self.player_on_turn, "End"]:
                    if copied_board[i+1][symbol_index] in [self.player_on_turn, "End"] and copied_board[i+2][symbol_index] in [self.player_on_turn, "End"]:
                        for a in range(-2, 3):
                            self.win_symbols.append((i+a, symbol_index))
                        return 1

    def _diagonal_win(self):
        copied_board = deepcopy(self.board)
        for i, row in enumerate(copied_board[2:18]):
            i += 2
            for _ in range(row.count(self.player_on_turn)):
                symbol_index = row.index(self.player_on_turn)
                row[row.index(self.player_on_turn)] = "End"
                if symbol_index >= 2 and symbol_index <= self.board_size - 3:
                    if copied_board[i-2][symbol_index-2] in [self.player_on_turn, "End"] and copied_board[i-1][symbol_index-1] in [self.player_on_turn, "End"]:
                        if copied_board[i+1][symbol_index+1] in [self.player_on_turn, "End"] and copied_board[i+2][symbol_index+2] in [self.player_on_turn, "End"]:
                            for a in range(-2, 3):
                                self.win_symbols.append((i+a, symbol_index+a))
                            return 1
                    elif copied_board[i-2][symbol_index+2] in [self.player_on_turn, "End"] and copied_board[i-1][symbol_index+1] in [self.player_on_turn, "End"]:
                        if copied_board[i+1][symbol_index-1] in [self.player_on_turn, "End"] and copied_board[i+2][symbol_index-2] in [self.player_on_turn, "End"]:
                            for a in range(-2, 3):
                                self.win_symbols.append((i+a, symbol_index-a))
                            return 1

    def _is_tie(self):
        for row in self.board:
            if row.count("·") >= 1:
                return 0
        return 2



    def game_ended(self):
        if self._horizontal_win() or self._vertical_win() or self._diagonal_win():
            self.winner = self.player_on_turn
            return 1
        elif self._is_tie():
            return 2





