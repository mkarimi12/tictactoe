class TicTacToe:
    def __init__(self, current_board=None, turn='X', is_simulated=False):
        if current_board is None:
            self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.count = 0
        else:
            current_count = 0
            self.game_board = current_board
            for ch in current_board:
                if ch != ' ':
                    current_count += 1
            self.count = current_count

        self.turn = turn
        self.is_simulated = is_simulated

        self.we_are = 'X'
        self.rival_is = 'O'

    # def action(self, state, turn):
    #     next_turn = 'X' if turn == 'O' else 'O'

    def find_children(self):
        children = []
        if self.is_simulated:
            next_turn = 'X' if self.turn == 'O' else 'O'
        else:
            next_turn = self.turn
        for idx, ch in enumerate(self.game_board):
            if ch == ' ':
                child = self.game_board.copy()

                child[idx] = next_turn
                ch_obj = TicTacToe(current_board=child, turn=next_turn, is_simulated=True)
                children.append(ch_obj)
        return children

    def play(self, pos, turn):
        if not self.is_valid_move(pos):
            raise InvalidMove("Invalid move!")
        else:
            self.count += 1
            if turn == 'X' or turn == 'x':
                self.game_board[pos] = 'X'
            else:
                self.game_board[pos] = 'O'

    def is_valid_move(self, pos):
        return True if self.game_board[pos] == ' ' else False

    def terminal_state(self, lx):
        victory = 1 if lx == self.we_are else -1
        terminal = None
        if self.count == 9:
            terminal = 0
        elif self.count >= 5:
            winner = (self.game_board[0] == self.game_board[1] == self.game_board[2] == lx) or \
                     (self.game_board[3] == self.game_board[4] == self.game_board[5] == lx) or \
                     (self.game_board[6] == self.game_board[7] == self.game_board[8] == lx) or \
                     (self.game_board[0] == self.game_board[3] == self.game_board[6] == lx) or \
                     (self.game_board[1] == self.game_board[4] == self.game_board[7] == lx) or \
                     (self.game_board[2] == self.game_board[5] == self.game_board[8] == lx) or \
                     (self.game_board[0] == self.game_board[4] == self.game_board[8] == lx) or \
                     (self.game_board[2] == self.game_board[4] == self.game_board[6] == lx)
            lo = 'O' if lx == 'X' else 'X'
            looser = (self.game_board[0] == self.game_board[1] == self.game_board[2] == lo) or \
                     (self.game_board[3] == self.game_board[4] == self.game_board[5] == lo) or \
                     (self.game_board[6] == self.game_board[7] == self.game_board[8] == lo) or \
                     (self.game_board[0] == self.game_board[3] == self.game_board[6] == lo) or \
                     (self.game_board[1] == self.game_board[4] == self.game_board[7] == lo) or \
                     (self.game_board[2] == self.game_board[5] == self.game_board[8] == lo) or \
                     (self.game_board[0] == self.game_board[4] == self.game_board[8] == lo) or \
                     (self.game_board[2] == self.game_board[4] == self.game_board[6] == lo)
            if winner:
                terminal = victory
            elif looser:
                terminal = -1 * victory

        return terminal

    def possible_move(self):
        pass

    def __str__(self):
        game_board_helper = [(idx + 1).__str__() if s == ' ' else s for idx, s in enumerate(self.game_board)]
        print(game_board_helper)
        string = """
         %c | %c | %c
        ---+---+---
         %c | %c | %c
        ---+---+---
         %c | %c | %c
        """ % tuple(game_board_helper)
        return string


class InvalidMove(Exception):
    pass
