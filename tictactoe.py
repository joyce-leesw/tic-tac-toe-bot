import random
class Tictactoe:
    def __init__ (self, render= True):
        self.board = [[0,0,0] for _ in range(3)]
        self.render = render
        self.player = random.choice([1, -1])
        self.repr = {0: ".", 1: "X", -1: "O"}

    # get player key
    def get_player(self):
        key = ''

        key = input("Please select your key. X or O?: ")
        key = key.upper()

        if key == 'X':
            self.player *= -1
        print(f"Your key is {key}")
        return key

    # check if there exists a winner
    def is_winner(self):
        win = None
        # rows
        for row in range(3):
            if abs(sum(self.board[row])) == 3:
                win = self.board[row][0]

        # columns    
        for column in range(3):
            if abs(sum([row[column] for row in self.board]))  == 3:
                win = self.board[0][column]

        # diagonals
        if abs(sum([self.board[row][row] for row in range(3)])) == 3:
            win = self.board[0][0]

        if abs(sum([self.board[row][2- row] for row in range(3)])) == 3:
            win = self.board[0][2]

        return win
    
    # return state of board
    def cur_state(self):
        return str(self.board)
    
    def next_state(self, x, y):
        next_state = self.board.copy()
        next_state[x][y] = self.player
        return str(next_state)

    # check for valid moves
    def get_valid_moves(self):
        move = []
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    move.append((row, column))
        return move

    # check if game has ended
    def get_end(self):
        if self.is_winner() is not None:
            return True
        
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    return False
        return True
    
    # print board
    def show_board(self):
        for row in self.board:
            for column in row:
                print(self.repr[column], end="\t")
            print("\n")
        print("-----------------\n")

    # ensure no illegal moves, player changes after every move
    def play(self, x, y):
        if self.board[x][y] != 0:
            return None
        self.board[x][y] = self.player
        if self.render:
            self.show_board()
        if self.is_winner():
            return self.is_winner()
        self.player *= -1
        return None
