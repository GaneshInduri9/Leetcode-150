"""
    Given an n x n array of integers matrix, return the minimum sum of any
    falling path through matrix. A falling path starts at any element in the first
    row and chooses the element in the next row that is either directly below or diagonally
    left/right. Specifically, the next element from position (row, col) will be 
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""
from typing import List
class Solution:
    """
        Again the idea is brute force it either we can start from bottom row
        or starting row either of that works out. If we start from and or col
        is in range then that means we are good we can return our base case but
        if the boundary goes out of bound then we need to return.

        If a decision tree is drawn for this we can see there are overlapping sub
        problems so we memo it.
    """
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        min_path = float('inf')
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(r,c):
                
            if c < 0 or c >m-1:
                return float('inf')

            if r == n-1:
                return matrix[r][c]

            if memo[r][c] != -1:
                return memo[r][c]
            
            b = matrix[r][c] + dfs(r+1, c)
            ld = matrix[r][c] + dfs(r+1, c-1)
            rd =  matrix[r][c] + dfs(r+1, c+1 )
            memo[r][c] = min(b, ld, rd) 
            return min(b, ld, rd)
        for i in range(m):
            min_path = min(min_path, dfs(0,i))
        return min_path

    def minFallingPathSumTab(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            memo[0][i] = matrix[0][i]
        
        for i in range(1,n):
            for j in range(m):
                above = matrix[i][j] + memo[i-1][j]
                leftDg = float('inf')
                if j>0:
                    leftDg = matrix[i][j] + memo[i-1][j-1]
                
                rightDg = float('inf')

                if j < m-1:
                    rightDg = matrix[i][j] + memo[i-1][j+1]
                memo[i][j] = min(leftDg, rightDg, above)
            
        return min(memo[-1])

def test_min_falling_path_sum():
    solution = Solution()

    # Test case 1: Small matrix (1x1)
    matrix = [[7]]
    assert solution.minFallingPathSum(matrix) == 7
    assert solution.minFallingPathSumTab(matrix) == 7

    # Test case 2: Simple 2x2 matrix
    matrix = [
        [2, 1],
        [3, 4]
    ]
    assert solution.minFallingPathSum(matrix) == 4  # Path: (0,1) -> (1,0)
    assert solution.minFallingPathSumTab(matrix) == 4

    # Test case 3: Simple 3x3 matrix
    matrix = [
        [2, 3, 1],
        [6, 5, 4],
        [7, 8, 9]
    ]
    assert solution.minFallingPathSum(matrix) == 13  # Path: (0,2) -> (1,2) -> (2,2)
    assert solution.minFallingPathSumTab(matrix) == 13

    # Test case 4: Matrix with negative values
    matrix = [
        [-19, 57],
        [-40, -5]
    ]
    assert solution.minFallingPathSum(matrix) == -59  # Path: (0,0) -> (1,0)
    assert solution.minFallingPathSumTab(matrix) == -59

    # Test case 5: Larger matrix
    matrix = [
        [2, 3, 4],
        [5, 6, 7],
        [8, 9, 10],
        [11, 12, 13]
    ]
    assert solution.minFallingPathSum(matrix) == 26  # Path: (0,0) -> (1,0) -> (2,0) -> (3,0)
    assert solution.minFallingPathSumTab(matrix) == 26

    # Test case 6: Edge case with all elements equal
    matrix = [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
    assert solution.minFallingPathSum(matrix) == 15  # Any path gives the same sum
    assert solution.minFallingPathSumTab(matrix) == 15

    # Test case 7: Large negative values
    matrix = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    assert solution.minFallingPathSum(matrix) == -18  # Path: (0,2) -> (1,2) -> (2,2)
    assert solution.minFallingPathSumTab(matrix) == -18

    print("All test cases passed!")

test_min_falling_path_sum()
