"""
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and
    '0's (water), return the number of islands.An island is surrounded by water and 
    is formed by connecting adjacent lands horizontally or vertically. You 
    may assume all four edges of the grid are all surrounded by water.
"""
from typing import List
class Solution:
    """
        The intution behind this we have obeserve that this is kind of graph problem 
        because each of the islands is kind of group of connected cities. so if we find
        city than explore all it's neighbours. So the answer is conut of how many times we 
        explore the cities. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1'):
                    count += 1
                    self.dfs(grid, i,j)
        return count
    
    def dfs(self, grid: List[List[str]], r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)



# The Solution class definition is assumed to be above this point.

# Instantiate the Solution
sol = Solution()

# Test case 1: Basic grid with a single island
grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
assert sol.numIslands(grid1) == 1, "Test case 1 failed."

# Test case 2: Grid with multiple islands
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
assert sol.numIslands(grid2) == 3, "Test case 2 failed."

# Test case 3: Grid with no islands
grid3 = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
assert sol.numIslands(grid3) == 0, "Test case 3 failed."

# Test case 4: Single cell grid with an island
grid4 = [["1"]]
assert sol.numIslands(grid4) == 1, "Test case 4 failed."

# Test case 5: Single cell grid with no island
grid5 = [["0"]]
assert sol.numIslands(grid5) == 0, "Test case 5 failed."

# Test case 6: Grid with islands connected diagonally (should not count as one island)
grid6 = [
    ["1", "0", "0", "0"],
    ["0", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "0", "0", "1"]
]
assert sol.numIslands(grid6) == 4, "Test case 6 failed."

# Test case 7: Large grid with one large island
grid7 = [
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"]
]
assert sol.numIslands(grid7) == 1, "Test case 7 failed."

print("All test cases passed!")
