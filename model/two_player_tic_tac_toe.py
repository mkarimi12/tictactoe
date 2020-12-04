from .tic_tac_toe import TicTacToe, InvalidMove


class TwoPlayersTicTacToe(TicTacToe):
    def game_play_2_person(self):
        print(self.__str__())
        count = 0
        while count <= 9:

            print("It's '%s' turn, please enter a number?" % self.turn)
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
            self.find_children()
            status = self.terminal_state(self.turn)
            if status == 1:
                print("'%s' won the game!!" % self.turn)
                break
            elif status == 0:
                print("It's a tie!")
                break

            count += 1
            self.turn = 'O' if self.turn == 'X' else 'X'


# class InvalidMove(Exception):
#     pass
