from typing import List
from collections import deque


class Solution:

    def shortestPath(
        self, grid: List[List[int]], source: List[int], destination: List[int]
    ) -> int:
        # code here
        r = len(grid)
        c = len(grid[0])
        q = deque()
        q.append((source[0], source[1], 0))  # ({r,c}, 0)
        vis = set()
        vis.add((source[0], source[1]))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            curR, curC, dist = q.popleft()

            if (curR, curC) == (destination[0], destination[1]):
                return dist

            for dr, dc in directions:
                newR = curR + dr
                newC = curC + dc

                if (
                    newR < r
                    and newR >= 0
                    and newC < c
                    and newC >= 0
                    and grid[newR][newC] != 0
                    and (newR, newC) not in vis
                ):
                    q.append((newR, newC, dist + 1))
                    vis.add((newR, newC))

        return -1


# Test cases
sol = Solution()

# Test Case 1: Basic Case (Path Exists)
grid1 = [[1, 1, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1]]
source1 = [0, 0]
destination1 = [2, 3]
print(sol.shortestPath(grid1, source1, destination1))  # Expected output: 5

# Test Case 2: No Path Exists (Blocked Destination)
grid2 = [[1, 1, 1], [1, 0, 1], [1, 1, 0]]
source2 = [0, 0]
destination2 = [2, 2]
print(sol.shortestPath(grid2, source2, destination2))  # Expected output: -1

# Test Case 3: Source is Same as Destination
grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
source3 = [1, 1]
destination3 = [1, 1]
print(sol.shortestPath(grid3, source3, destination3))  # Expected output: 0

# Test Case 4: Single Row Path
grid4 = [[1, 1, 1, 1, 1]]
source4 = [0, 0]
destination4 = [0, 4]
print(sol.shortestPath(grid4, source4, destination4))  # Expected output: 4

# Test Case 5: Single Column Path
grid5 = [[1], [1], [1], [1], [1]]
source5 = [0, 0]
destination5 = [4, 0]
print(sol.shortestPath(grid5, source5, destination5))  # Expected output: 4

# Test Case 6: Grid with No 1s
grid6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
source6 = [0, 0]
destination6 = [2, 2]
print(sol.shortestPath(grid6, source6, destination6))  # Expected output: -1

# Test Case 7: Source or Destination Blocked
grid7 = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
source7 = [0, 0]  # Blocked
destination7 = [2, 2]
print(sol.shortestPath(grid7, source7, destination7))  # Expected output: -1

grid8 = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]  # Destination is blocked
source8 = [0, 0]
destination8 = [2, 2]
print(sol.shortestPath(grid8, source8, destination8))  # Expected output: -1

# Test Case 8: Larger Grid with a Path
grid9 = [[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1]]
source9 = [0, 0]
destination9 = [3, 5]
print(
    sol.shortestPath(grid9, source9, destination9)
)  # Expected output: Shortest distance (varies)
