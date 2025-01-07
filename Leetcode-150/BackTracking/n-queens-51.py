from typing import List
class Solution:
    """
        The idea is to see if we can place Q in current col
        if we can place it what we can do is try to place
        the col in the next col if we ever reach the end that means
        we were able to place Q according to the conditions
        if we can't place then what we do is try another row in same col
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        left_set =[0]*n
        lower_diagnol = [0]*((2*n)-1)
        bottom_diagnol = [0]*((2*n)-1)
        def backTrack(col):
            if col == n:
                res.append([''.join(row) for row in board])
                return

            for r in range(n):
                if left_set[r] == 0 and lower_diagnol[r+col] == 0 and bottom_diagnol[n-1+col-r] == 0:
                    board[r][col] = 'Q'
                    left_set[r] = 1
                    lower_diagnol[r+col] = 1
                    bottom_diagnol[n-1+col-r] = 1
                    backTrack(col+1)
                    board[r][col] = '.'
                    left_set[r] = 0
                    lower_diagnol[r+col] = 0
                    bottom_diagnol[n-1+col-r] = 0

        backTrack(0)
        return res

import unittest

class TestSolveNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        """Test for n = 1."""
        expected = [['Q']]
        self.assertEqual(self.solution.solveNQueens(1), expected)

    def test_n_2(self):
        """Test for n = 2 (no solution expected)."""
        expected = []
        self.assertEqual(self.solution.solveNQueens(2), expected)

    def test_n_3(self):
        """Test for n = 3 (no solution expected)."""
        expected = []
        self.assertEqual(self.solution.solveNQueens(3), expected)

    def test_n_4(self):
        """Test for n = 4 (two solutions expected)."""
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        self.assertEqual(sorted(self.solution.solveNQueens(4)), sorted(expected))

    def test_n_5(self):
        """Test for n = 5."""
        result = self.solution.solveNQueens(5)
        # Check that there are 10 solutions for n = 5
        self.assertEqual(len(result), 10)

if __name__ == "__main__":
    unittest.main()
