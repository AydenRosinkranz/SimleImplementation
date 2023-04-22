import random
from Agent_Player import GameStatus
from Agent_Player import HumanPlayer
from Agent_Player import ComputerPlayer
def main():
    player1 = HumanPlayer('X')
    player2 = ComputerPlayer('O')
    game_status = GameStatus()
    game_status.current_player = random.choice(['X', 'O'])
    while not game_status.game_over:
        if game_status.current_player == player1.symbol:
            row, col = player1.get_move(game_status)
            game_status.make_move(row, col, player1.symbol)
        else:
            row, col = player2.get_move(game_status)
            game_status.make_move(row, col, player2.symbol)
        print_board(game_status.board)
    if game_status.winner:
        print(f"{game_status.winner} wins!")
    else:
        print("Tie game.")


def print_board(board):
    print('-' * 9)
    for row in board:
        print('|', end=' ')
        for col in row:
            print(col, end=' ')
        print('|')
    print('-' * 9)


if __name__ == '__main__':
    main()
