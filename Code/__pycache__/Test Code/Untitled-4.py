class ConnectionsGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 1

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = str(self.current_player)
            self.current_player = 3 - self.current_player  # Switch player

    def is_game_over(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == ' ':
                    return False
        return True

# Example usage:
game = ConnectionsGame(3, 3)

while not game.is_game_over():
    game.print_board()
    row = int(input(f'Player {game.current_player}, enter row: '))
    col = int(input(f'Player {game.current_player}, enter col: '))
    game.make_move(row, col)

print("Game over!")

