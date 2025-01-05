"""
    Given an m x n grid of characters board and a string word, return 
    true if word exists in the grid.The word can be constructed from letters 
    of sequentially adjacent cells, where adjacent cells are horizontally or 
    vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List
class Solution:

    """
        So what's the brute force way to solve imagine how ur going to solve this in the most brute force
        way, we would want to start at the start of the board and see if this is the starting of the word
        that we are looking for if that charecter at that position is start of the word then we have to look
        around it's neighbours if they match with next charceter in the word, okay they match then what just 
        look for the next word on the board with the current neighbours but don't want to revisit them 
        again so what do we do just remember what we had just visited so that we don't come back again to the 
        same position even if we comback it this will be in the set so we don't looking in that path we can do 
        this without set as well so we can put # symbol or something and when coming from that we can 
        pop the element that we have just added.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows, cols = len(board), len(board[0])
        word_len = len(word)
        def dfs(r, c, i):

            if i == word_len:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in path or board[r][c] != word[i]:
                return False

            path.add((r,c)) # board[r][c] = #
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r,c)) # backtrack from here :board[r][c] = word[i]
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False

def test_exist():
    solution = Solution()

    # Test case 1: Simple positive case
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    assert solution.exist(board1, word1) == True, "Test case 1 failed"

    # Test case 2: Simple negative case
    word2 = "ABCB"
    assert solution.exist(board1, word2) == False, "Test case 2 failed"

    # Test case 3: Word exists diagonally (not valid)
    word3 = "ABE"
    assert solution.exist(board1, word3) == False, "Test case 3 failed"

    # Test case 4: Single character word exists
    word4 = "E"
    assert solution.exist(board1, word4) == True, "Test case 4 failed"

    # Test case 5: Single character word does not exist
    word5 = "Z"
    assert solution.exist(board1, word5) == False, "Test case 5 failed"

    # Test case 6: Word spans entire board
    board2 = [
        ['A', 'B'],
        ['C', 'D']
    ]
    word6 = "ABCD"
    assert solution.exist(board2, word6) == False, "Test case 6 failed"

    # Test case 7: Larger board, word exists
    board4 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word9 = "ABCESEEEFS"
    assert solution.exist(board4, word9) == True, "Test case 9 failed"

    # Test case 10: Larger board, word does not exist
    word10 = "ABCESEEEEZ"
    assert solution.exist(board4, word10) == False, "Test case 10 failed"

    print("All test cases passed!")

test_exist()

            