import unittest
from tictactoe import Board

class TestBoardState(unittest.TestCase):

    def test_newboard(self):
        """New boards should be empty"""
        board = Board()
        self.assertEqual("".join(board.gs), " " * 9)
        for i in range(0, 9):
            board.inputMove(i, "X")
        board.__init__()
        self.assertEqual("".join(board.gs), " " * 9)

    def test_winconditions(self):
        """Make sure all win conditions are valid"""
        board = Board()
        """Testing top row win"""
        for i in range(0,3):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing middle row win"""
        for i in range(3, 6):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing bottom row win"""
        for i in range(6, 9):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing left vertical column win"""
        for i in range(0, 7, 3):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing middle vertical column win"""
        for i in range(1, 8, 3):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing right vertical column win"""
        for i in range(2, 9, 3):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing \ diagonal win"""
        for i in range(0, 9, 4):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

        """Testing / diagonal win"""
        for i in range(2, 7, 2):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForWinner("X"))
        board.__init__

    def test_input(self):
        """Confirm inputMove properly encodes game data"""
        board = Board()
        board.inputMove(5, "X")
        self.assertEqual(board.gs[5], "X")
        self.assertEqual(board.gs[4], " ")
        self.assertEqual(board.gs[6], " ")

    def test_draw(self):
        """Confirm Board object correctly determines a draw state"""
        board = Board()
        self.assertFalse(board.checkForDraw())
        for i in range(0,9):
            board.inputMove(i, "X")
        self.assertTrue(board.checkForDraw())

if __name__ == '__main__':
    unittest.main()
