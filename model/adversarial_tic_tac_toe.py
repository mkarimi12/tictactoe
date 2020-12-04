from .tic_tac_toe import TicTacToe, InvalidMove


class Adversarial(TicTacToe):
    def __init__(self, game_board=None):
        super().__init__(game_board, is_simulated=False)

    def utility_func(self, state):
        return state.terminal_state(self.turn)

    def terminal_test(self, state):
        return False if state.terminal_state(self.turn) is None else True

    def action(self):
        pass

    def maximize(self, state):
        if self.terminal_test(state):
            return None, self.utility_func(state)

        (max_child, max_util) = None, -1000

        for child in state.find_children():
            (_, util) = self.minimize(child)
            if util > max_util:
                (max_child, max_util) = child, util
        return max_child, max_util

    def minimize(self, state):
        if self.terminal_test(state):
            return None, self.utility_func(state)

        (min_child, min_util) = None, +1000
        children = state.find_children()
        for child in children:
            (_, util) = self.maximize(child)
            if util < min_util:
                (min_child, min_util) = child, util

        return min_child, min_util

    def decision(self, state):
        child, util = self.minimize(state)
        for idx, st in enumerate(state.game_board):
            if child.game_board[idx] != state.game_board[idx]:
                return idx + 1

    # return child

    def game_play(self):
        print(self.__str__())
        count = 0
        while count <= 9:
            # HUMAN turn
            print("It's '%s' turn, please enter a number?" % 'X')
            move = int(input())
            try:
                self.play(move - 1, self.turn)
            except InvalidMove:
                print("You have done an Invalid move! Please move again.")
                continue
            print(self.__str__())
            # if self.is_winner(self.turn):
            #     print("'%s' won the game!!" % self.turn)
            #     break
            # elif self.is_tie():
            #     print("It's a tie!")
            #     break
            # self.find_children()
            status = self.terminal_state(self.turn)
            if status == 1:
                print("'%s' won the game!!" % self.turn)
                break
            if status == -1:
                print("'%s' won the game!!" % self.turn)
                break
            elif status == 0:
                print("It's a tie!")
                break

            count += 1
            self.turn = 'O' if self.turn == 'X' else 'X'

            # MACHINE turn
            # print("It's '%s' turn, please enter a number?" % self.turn)
            dec = self.decision(self)
            # print("dec", dec)
            # self.turn = 'O' if self.turn == 'X' else 'X'

            self.play(dec - 1, self.turn)
            print(self.__str__())
            # self.find_children()
            status = self.terminal_state(self.turn)
            if status == 1:
                print("'%s' won the game!!" % self.turn)
                break
            if status == -1:
                print("'%s' won the game!!" % self.turn)
                break
            elif status == 0:
                print("It's a tie!")
                break

            count += 1
            self.turn = 'O' if self.turn == 'X' else 'X'
