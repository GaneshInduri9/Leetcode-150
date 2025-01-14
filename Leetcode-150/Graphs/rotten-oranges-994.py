from collections import deque
from typing import List
class Solution:
    """
        Here dfs would never work out we would go as deep possible and comeback that would never lead us to 
        the answer. Think of it like this what if you have a source node and u have to visit each level at time
        each level actual indicates the time to visit all the neighbours so what algorithm that comes to ur mind 
        when you want all the neighbours to be proccessed at once it's bfs right we rot all the neighbours for rotten orrange
        to rot and then make the other neighbours to rot from this rotten orange.

        Note that we might have multiple oranges rotted in trhe begining stage so we need to keep track of all the rotten oranges
        and try rot from the each posiston at same time.
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # edge case
        if len(grid) == 0:
            return 0
        
        # required variables and Data struct's
        q = deque()
        time = 0
        fresh = 0 # to count how many fresh oranges are there and to check if we are able rot all of them.
        m = len(grid)
        n = len(grid[0])
        v = []
        for _ in range(m):
            v.append([0] *n)
        
        # Append all intial rotten oranges so that we can do BFS from each start.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    v[i][j] = 1
                    q.append(((i,j),0))
        
        # above col, below col, left row, right row
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            # {(r,j), time}
            (curr, t) = q.popleft()
            curR, curC = curr
            time = max(t,time)

            for dr, dc in directions:

                newR = curR +  dr
                newC = curC + dc
                # make sure that this doesn't go out of bound and not visited and not a 0.
                if newR >= 0 and newR < m and newC >= 0 and newC < n and v[newR][newC] != 1 and grid[newR][newC] == 1:
                    v[newR][newC] = 1
                    q.append(((newR,newC),t+1))
                    # able to a fresh orange so decrement it.
                    fresh -=1 
                
        
        # -1 if not able reach any fresh orange.
        return -1 if fresh != 0 else time

def test_oranges_rotting():
    solution = Solution()

    test_cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),  # Basic test
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1), # All fresh oranges
        ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0),  # All rotten oranges
        ([[2, 0, 1], [0, 0, 0], [1, 0, 1]], -1), # Mixed with empty cells
        ([[2, 0, 0], [0, 2, 0], [0, 0, 2]], 0),  # No fresh oranges
        ([[2]], 0),                              # Single cell, rotten
        ([[1]], -1),                             # Single cell, fresh
        ([[0]], 0),                              # Single cell, empty
        ([], 0),                                 # Empty grid
        ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 1)  # Fresh surrounded by rotten
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.orangesRotting(grid)
        print(f"Test Case {i}: {'Passed' if result == expected else f'Failed (Expected {expected}, Got {result})'}")

# Run the test function
test_oranges_rotting()
                
        

