"""
Python TicTacToe game
"""
class TicTacToe:
    "this class describes a single TicTacToe game"

    def __init__(self):
        self.board = [[" " for _ in range(3)] for i in range(3)]
        self.x_coord = 0
        self.y_coord = 0
        self.check_moves = 0

    def show_board(self):
        "this function displays a grid"
        print("---------")
        print("|", self.board[0][0], self.board[0][1], self.board[0][2], "|")
        print("|", self.board[1][0], self.board[1][1], self.board[1][2], "|")
        print("|", self.board[2][0], self.board[2][1], self.board[2][2], "|")
        print("---------")

    def start_game(self):
        "this function takes the coordinates of the cell"
        self.x_coord, self.y_coord = input("Enter the coordinates:").split()

    def validate_input(self):
        "this function checks whether it was a valid input or not"
        if (self.x_coord.count(".") == 1 and self.x_coord.replace(".", "").isdigit()):
            print("You should enter integers!")
            return False
        if (not self.x_coord.isdigit() or not self.y_coord.isdigit()):
            print("You should enter numbers!")
            return False
        int_x = int(self.x_coord)
        int_y = int(self.y_coord)
        if (int_x < 1 or int_x > 3) or (int_y < 1 or int_y > 3):
            print("Coordinates should be from 1 to 3!")
            return False
        if self.board[int_x - 1][int_y - 1] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def fill_process(self):
        "this function determines who will make a move"
        if self.check_moves % 2 == 1:
            self.board[int(self.x_coord) - 1][int(self.y_coord) - 1] = "X"
        else:
            self.board[int(self.x_coord) - 1][int(self.y_coord) - 1] = "O"

    def check_winner(self):
        "this function checks if someone already wins or not"
        int_x = int(self.x_coord) - 1
        int_y = int(self.y_coord) - 1
        x_wins = 0
        o_wins = 0
        if self.board[int_x][0] == self.board[int_x][1] == self.board[int_x][2] == "X":
            x_wins = True
        if self.board[int_x][0] == self.board[int_x][1] == self.board[int_x][2] == "O":
            o_wins = True
        if self.board[0][int_y] == self.board[1][int_y] == self.board[2][int_y] == "X":
            x_wins = True
        if self.board[0][int_y] == self.board[1][int_y] == self.board[2][int_y] == "O":
            o_wins = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == "X":
            x_wins = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == "X":
            x_wins = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == "O":
            o_wins = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == "O":
            o_wins = True
        if x_wins:
            return "X wins"
        if o_wins:
            return "O wins"
        if self.check_moves == 9:
            return "Draw"
        return False

    def game_process(self):
        "this function show the process of the game"
        while True:
            self.start_game()
            while self.validate_input() is False:
                self.start_game()
            self.check_moves += 1
            self.fill_process()
            self.show_board()
            if self.check_winner() is not False:
                break
            if self.check_winner() is False:
                continue
        print(self.check_winner())

if __name__ == "__main__":
    game = TicTacToe()
    game.game_process()
