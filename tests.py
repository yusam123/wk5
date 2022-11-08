import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_create_board(self):
        board = [0,0,0,
        0,0,0,
        0,0,0]
        self.assertEqual(logic.create_board(), board)

    def test_win_check(self):
        player = [2,5]
        for x in player:
            board0 = [x,0,0,
            0,x,0,
            0,0,x]
            board1 = [x,x,x,
            0,0,0,
            0,0,0]
            board2 = [x,0,0,
            x,0,0,
            x,0,0]
            board3 = [0,0,x,
            0,x,0,
            x,0,0]
            self.assertEqual(logic.win_check(board0), x)
            self.assertEqual(logic.win_check(board1), x)
            self.assertEqual(logic.win_check(board2), x)
            self.assertEqual(logic.win_check(board3), x)
        board4 = [2,2,0,
            0,5,0,
            5,0,2]
        self.assertEqual(logic.win_check(board4), 0)

if __name__ == '__main__':
    unittest.main()