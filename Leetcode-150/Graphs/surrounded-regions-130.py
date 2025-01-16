from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Solves the surrounded regions problem: Flips all 'O's not connected to the boundary to 'X'.
        
        Time Complexity: O(n * m), where n = rows and m = cols in the board.
        Space Complexity: O(n * m) for the visited matrix and recursion stack.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]  # Visited matrix
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Directions for traversal

        def dfs(r, c):
            visited[r][c] = 1
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                # Explore only valid and unvisited 'O' cells
                if 0 <= newR < rows and 0 <= newC < cols and visited[newR][newC] == 0 and board[newR][newC] == 'O':
                    dfs(newR, newC)

        # Process the first and last rows
        for j in range(cols):
            if board[0][j] == 'O' and visited[0][j] == 0:
                dfs(0, j)
            if board[rows - 1][j] == 'O' and visited[rows - 1][j] == 0:
                dfs(rows - 1, j)

        # Process the first and last columns
        for i in range(rows):
            if board[i][0] == 'O' and visited[i][0] == 0:
                dfs(i, 0)
            if board[i][cols - 1] == 'O' and visited[i][cols - 1] == 0:
                dfs(i, cols - 1)

        # Flip unvisited 'O' to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    board[i][j] = 'X'

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Counts the number of 1s in the grid that are not connected to the boundary.
        
        Time Complexity: O(n * m), where n = rows and m = cols in the grid.
        Space Complexity: O(n * m) for the visited matrix and queue.
        """
        n = len(grid)
        m = len(grid[0])
        v = [[0 for _ in range(m)] for _ in range(n)]  # Visited matrix
        q = deque()  # Queue for BFS
        res = 0

        # Mark boundary-connected cells
        for j in range(m):
            if grid[0][j] == 1:
                q.append((0, j))
                v[0][j] = 1
            if grid[n - 1][j] == 1:
                q.append((n - 1, j))
                v[n - 1][j] = 1
        
        for i in range(n):
            if grid[i][0] == 1:
                q.append((i, 0))
                v[i][0] = 1
            if grid[i][m - 1] == 1:
                q.append((i, m - 1))
                v[i][m - 1] = 1

        # BFS to mark all boundary-connected 1s
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < n and 0 <= newC < m and v[newR][newC] == 0 and grid[newR][newC] == 1:
                    v[newR][newC] = 1
                    q.append((newR, newC))
                
        # Count all unvisited 1s
        for i in range(n):
            for j in range(m):
                if v[i][j] == 0 and grid[i][j] == 1:
                    res += 1

        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test for `solve`
    print("Testing `solve` function:")
    board1 = [["X", "X", "X", "X"],
              ["X", "O", "O", "X"],
              ["X", "X", "O", "X"],
              ["X", "O", "X", "X"]]
    sol.solve(board1)
    print("Result:")
    for row in board1:
        print(row)
    # Expected:
    # [["X", "X", "X", "X"],
    #  ["X", "X", "X", "X"],
    #  ["X", "X", "X", "X"],
    #  ["X", "O", "X", "X"]]

    board2 = [["O", "O", "O"],
              ["O", "O", "O"],
              ["O", "O", "O"]]
    sol.solve(board2)
    print("Result:")
    for row in board2:
        print(row)
    # Expected:
    # [["O", "O", "O"],
    #  ["O", "O", "O"],
    #  ["O", "O", "O"]]

    # Test for `numEnclaves`
    print("\nTesting `numEnclaves` function:")
    grid1 = [[0, 0, 0, 0],
             [1, 0, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
    print("Number of enclaves:", sol.numEnclaves(grid1))
    # Expected: 0

    grid2 = [[0, 1, 1, 0],
             [1, 0, 1, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]
    print("Number of enclaves:", sol.numEnclaves(grid2))
    # Expected: 3
