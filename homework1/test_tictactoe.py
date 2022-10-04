"""
unittest for game TicTacToe
"""
import unittest
from tictactoe import TicTacToe

class TestTictactoe(unittest.TestCase):
    "unittest class"

    def test_validate_input(self):
        "these tests check whether it was a valid input or not"
        game = TicTacToe()
        game.x_coord = "1.25"
        game.y_coord = "0.567923"
        self.assertFalse(game.validate_input())
        game.x_coord = "a"
        game.y_coord = "b"
        self.assertFalse(game.validate_input())
        game.x_coord = "2"
        game.y_coord = "100"
        self.assertFalse(game.validate_input())
        game.board[0][0] = "X"
        game.x_coord = "1"
        game.y_coord = "1"
        self.assertFalse(game.validate_input())

        game.board[1][1] = " "
        game.x_coord = "2"
        game.y_coord = "2"
        self.assertTrue(game.validate_input())
        
        game.x_coord = "2"
        game.y_coord = "2"
        game.fill_process()
        self.assertFalse(game.validate_input())

    def test_check_winner(self):
        "these tests check if someone already wins or not"
        game = TicTacToe()
        game.x_coord = "2"
        game.y_coord = "2"
        game.board[1][0] = game.board[1][1] = game.board[1][2] = "X"
        self.assertEqual(game.check_winner(), "X wins")
        game.x_coord = "3"
        game.y_coord = "3"
        game.board[0][2] = game.board[1][2] = game.board[2][2] = "O"
        self.assertEqual(game.check_winner(), "O wins")
        game.board[0][2] = game.board[1][1] = game.board[2][0] = "X"
        self.assertEqual(game.check_winner(), "X wins")
        game.board[0][0] = game.board[0][2] = "X"
        game.board[1][1] = game.board[1][2] = game.board[2][1] = "X"
        game.board[0][1] = game.board[1][0] = game.board[2][0] = game.board[2][2] = "O"
        game.check_moves = 9
        self.assertEqual(game.check_winner(), "Draw")
        
        game.x_coord = "3"
        game.y_coord = "3"
        game.board[0][2] = game.board[1][2] = game.board[2][2] = "X"
        self.assertNotEqual(game.check_winner(), "O wins")
        game.board[0][0] = game.board[1][1] = game.board[2][2] = "X"
        self.assertNotEqual(game.check_winner(), "O wins")
        
if __name__ == "__main__":
    unittest.main()
