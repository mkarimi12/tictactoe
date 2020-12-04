from model.tic_tac_toe import TicTacToe
from model.two_player_tic_tac_toe import TwoPlayersTicTacToe
from model.adversarial_tic_tac_toe import Adversarial


def main():
    # game2player = TwoPlayersTicTacToe()
    # game2player.game_play_2_person()

    play_with_machine = Adversarial()
    play_with_machine.game_play()

    # game_board = TicTacToe(current_board=['X', 'O', 'X', 'O', 'O', ' ', 'X', 'X', 'O'])
    # print(game_board.__str__())
    # print(game_board.terminal_state('X'))

    # game.play(8, "X")
    # game.play(5, "O")
    # game.play(4, "X")
    # game.play(2, "O")
    # game.play(0, "X")
    # # game.play(7, 'O')
    # print(game)
    # print(game.is_winner('X'))


if __name__ == '__main__':
    main()
