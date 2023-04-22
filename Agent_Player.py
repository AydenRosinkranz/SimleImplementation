class GameStatus:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.game_over = False
        self.winner = None

    def make_move(self, row, col, symbol):
        self.board[row][col] = symbol
        self.switch_players()
        self.check_winner()

    def switch_players(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.current_player
                self.game_over = True
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.current_player
                self.game_over = True
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.current_player
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.current_player
            self.game_over = True
            return
        if all([all([ele==' ' for ele in row]) for row in self.board]):
            self.game_over = True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game_status):
        pass


class HumanPlayer(Player):
    def get_move(self, game_status):
        row = int(input("Enter row for computers: ")) - 1
        col = int(input("Enter column for computers: ")) - 1
        return row, col


class ComputerPlayer(Player):
    def __init__(self, symbol, num_simulations=1000):
        super().__init__(symbol)
        self.num_simulations = num_simulations
    def get_move(self,game_status):
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ")) - 1
        return row, col




