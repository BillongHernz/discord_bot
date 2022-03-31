

class TicTacToe:

    def __init__(self, curr_data=None, history=None):

        self.win = False
        self.tie = False
        self.moves = 0
        self.player = 2
        self.history = []
        self.error_msg = ""

        if curr_data is None:
            self.board = [[0]*3, [0]*3, [0]*3]
        else:
            self.board = curr_data

        if history is not None:
            self.history = history
            self.moves = len(history)

    def __add_move(self, row, col):

        if row > 3 or row < 0 or col > 3 or col < 0:
            self.error_msg = f"Invalid move (row={row}, col={col})"
            return False

        if self.board[row-1][col-1] != 0:
            self.error_msg = f"Position not empty (row={row}, col={col})"
            return False
        else:
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

            self.board[row - 1][col - 1] = self.player
            self.moves += 1
            self.history.append([row, col])

            return True

    def __check_row_win(self, row, col):

        check_col = [i for i in range(3)]
        check_col.remove(col-1)

        if self.board[row - 1][check_col[0]] == self.player and self.board[row - 1][check_col[1]] == self.player:
            self.win = True
            return True

        return False

    def __check_col_win(self, row, col):

        check_row = [i for i in range(3)]
        check_row.remove(row - 1)

        if self.board[check_row[0]][col - 1] == self.player and self.board[check_row[1]][col - 1] == self.player:
            self.win = True
            return True

        return False

    def __check_diag_win(self, row, col):

        diag_comb = [[i,i] for i in range(3)]
        diag_comb.append([0, 2])
        diag_comb.append([2, 0])

        if [row, col] in diag_comb:
            if row == col:
                check_pos = diag_comb[:3]
                check_pos.remove([row,col])

                if self.board[check_pos[0][0]][check_pos[0][1]] == self.player and self.board[check_pos[1][0]][check_pos[1][1]] == self.player:
                    self.win = True
                    return True
                if row == 1:
                    if self.board[diag_comb[-2][0]][diag_comb[-2][1]] == self.player and self.board[diag_comb[-1][0]][diag_comb[-1][1]] == self.player:
                        self.win = True
                        return True
            else:
                check_pos = diag_comb[-2:]
                check_pos.append([1, 1])
                check_pos.remove([row, col])

                if self.board[check_pos[0][0]][check_pos[0][1]] == self.player and self.board[check_pos[1][0]][check_pos[1][1]] == self.player:
                    self.win = True
                    return True

        return False

    def __check_win(self, row, col):

        return self.__check_col_win(row, col) or self.__check_row_win(row, col) or self.__check_diag_win(row, col)

    def __check_tie(self):

        if self.moves == 9:
            self.tie = True
            return True

        return False

    def new_match(self):
        self.win = False
        self.tie = False
        self.moves = 0
        self.player = 2
        self.history = []
        self.error_msg = ""
        self.board = [[0]*3, [0]*3, [0]*3]

    def input_move(self, row, col):

        if self.tie or self.win or self.moves == 9:
            print("Starting New Match with current move")
            self.new_match()

        if not self.__add_move(row, col):
            print(self.error_msg)
            return

        if self.__check_win(row, col):
            print(f"Player {self.player} has won!")
            return

        if self.__check_tie():
            print("Match is a tie! No possible moves left")

        return

    def ret_board(self):
        return self.board

    def has_winner(self):
        return self.win

    def has_tie(self):
        return self.__check_tie()

    def curr_player(self):
        return self.player

    def get_history(self):
        return self.history


def print_board(board):

    try:
        print_out = []
        for row in board:

            row_out = []
            for val in row:
                if val == 1:
                    row_out.append('X')
                elif val == 2:
                    row_out.append('O')
                else:
                    row_out.append(' ')

            print_out.append("|".join(row_out))

        return "\n" + "\n".join(print_out) + "\n"

    except Exception:
        return "Incorrect board"


if __name__ == '__main__':

    test = TicTacToe()
    print(print_board(test.ret_board()))

    test.input_move(1, 2)
    print(print_board(test.ret_board()))

    test.input_move(2, 2)
    print(print_board(test.ret_board()))

    test.input_move(3, 2)
    print(print_board(test.ret_board()))

    test.input_move(2, 1)
    print(print_board(test.ret_board()))

    test.input_move(2, 3)
    print(print_board(test.ret_board()))

    test.input_move(1, 1)
    print(print_board(test.ret_board()))

    test.input_move(3, 3)
    print(print_board(test.ret_board()))

    test.input_move(3, 3)
    print(print_board(test.ret_board()))

    test.input_move(3, 1)
    print(print_board(test.ret_board()))

    print(test.get_history())

    test.input_move(3, 1)
    print(print_board(test.ret_board()))
