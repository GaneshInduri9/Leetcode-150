from typing import List
class Solution:

    """
        pre: Make sure you had solved leetcode 62 and 63
        Migth think of greedy appraoch but that wouldn't work out as 
        we dont know what values we would face in the up or left.
        So the most brute force way would be try all the path's 
        starting from the m-1, n-1 and evey place we have two choices
        we can go above or left so this recursively true from every 
        position.
    """
    def minPathSumBruteForce(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i < 0 or j < 0:
                # when out of bound make sure we return some big value
                return float('inf')
            
            
            
            left = grid[i][j] + dfs(i,j-1)
            up = grid[i][j] + dfs(i-1, j)
            
            return min(up, left)

        return dfs(m-1, n-1)
    
    # if you draw a desison tree we know there are overlapping sub problems
    # that makes it ideal for memoziation
    def minPathSumMemo(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = []

        for _ in range(m):
            memo.append([0]*n)

        def dfs(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i < 0 or j < 0:
                return float('inf')
            
            if memo[i][j] != 0:
                return memo[i][j]
            
            
            left = grid[i][j] + dfs(i,j-1)
            up = grid[i][j] + dfs(i-1, j)
            memo[i][j] = min(left, up)
            return memo[i][j]

        return dfs(m-1, n-1)
    
    # build solution from start
    def minPathSumTab(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = []

        for _ in range(m):
            dp.append([0]*n)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    up = float('inf')
                    left = float('inf')

                    if i > 0:
                        up = grid[i][j] + dp[i-1][j]
                    if j > 0:
                        left = grid[i][j] +dp[i][j-1]
                    
                    dp[i][j] = min(up, left)
        return dp[m-1][n-1]
    
    def minPathSumOptimal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [0]*n

        for i in range(m):
            tmp = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    tmp[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up = int(1e9)
                    left = grid[i][j]
                    if j> 0:
                        left += tmp[j-1]
                    else:
                        left = int(1e9)
                    tmp[j] = min(up, left)
            prev = tmp
        return prev[n-1]



def test_minPathSum():
    solution = Solution()

    # Test case 1: Simple 2x2 grid
    grid = [
        [1, 2],
        [1, 1]
    ]
    assert solution.minPathSumBruteForce(grid) == 3, "Test case 1 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 3, "Test case 1 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 3, "Test case 1 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 3, "Test case 1 failed (Optimal Space)"

    # Test case 2: Single row
    grid = [
        [1, 3, 1]
    ]
    assert solution.minPathSumBruteForce(grid) == 5, "Test case 2 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 5, "Test case 2 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 5, "Test case 2 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 5, "Test case 2 failed (Optimal Space)"

    # Test case 3: Single column
    grid = [
        [1],
        [2],
        [3]
    ]
    assert solution.minPathSumBruteForce(grid) == 6, "Test case 3 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 6, "Test case 3 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 6, "Test case 3 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 6, "Test case 3 failed (Optimal Space)"

    # Test case 4: Larger grid
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert solution.minPathSumBruteForce(grid) == 7, "Test case 4 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 7, "Test case 4 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 7, "Test case 4 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 7, "Test case 4 failed (Optimal Space)"

    # Test case 5: Grid with all zeros
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert solution.minPathSumBruteForce(grid) == 0, "Test case 5 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 0, "Test case 5 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 0, "Test case 5 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 0, "Test case 5 failed (Optimal Space)"

    # Test case 6: Grid with increasing numbers
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.minPathSumBruteForce(grid) == 21, "Test case 6 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 21, "Test case 6 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 21, "Test case 6 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 21, "Test case 6 failed (Optimal Space)"

    # Test case 7: Single cell grid
    grid = [[42]]
    assert solution.minPathSumBruteForce(grid) == 42, "Test case 7 failed (Brute Force)"
    assert solution.minPathSumMemo(grid) == 42, "Test case 7 failed (Memoization)"
    assert solution.minPathSumTab(grid) == 42, "Test case 7 failed (Tabulation)"
    assert solution.minPathSumOptimal(grid) == 42, "Test case 7 failed (Optimal Space)"

    print("All test cases passed!")

# Run the tests
test_minPathSum()
