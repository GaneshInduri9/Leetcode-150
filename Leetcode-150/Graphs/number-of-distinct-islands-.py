from typing import List
class Solution:
    """
        The idea is to remember the shape and that to the distinct ways so we can just use a set to do that
        at every dfs if do base-r we would get the shape directions so if we have same shape directions the set 
        will ignore this shape.

        Pre: Number of islands
    """
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        v = [[0 for _ in range(m)] for _ in range(n)]
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        s = set()

        def dfs(r, c, baser, basec, shape):
            v[r][c] = 1
            shape.add((r - baser, c - basec))

            for dr, dc in directions:
                newR = dr + r
                newC = dc + c

                if (
                    0 <= newR < n and 0 <= newC < m
                    and v[newR][newC] == 0
                    and grid[newR][newC] == 1
                ):
                    dfs(newR, newC, baser, basec, shape)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not v[i][j]:
                    shape = set()  # Initialize shape as a set
                    # Start a DFS and record the shape of the island
                    dfs(i, j, i, j, shape)
                    s.add(frozenset(shape))  # Add the shape as a frozenset to the set

        return len(s)


# Driver Code with Test Cases
if __name__ == "__main__":
    test_cases = [
        {
            "grid": [
                [1, 1, 0, 0, 0],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0]
            ],
            "expected": 3  # Distinct islands with unique shapes
        },
        {
            "grid": [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            "expected": 1  # Single large island
        },
        {
            "grid": [
                [1, 0],
                [0, 1]
            ],
            "expected": 2  # Two distinct single-cell islands
        },
        {
            "grid": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "expected": 0  # No islands
        },
    ]

    for idx, test in enumerate(test_cases, 1):
        obj = Solution()
        result = obj.countDistinctIslands(test["grid"])
        print(f"Test Case {idx}: {'PASSED' if result == test['expected'] else 'FAILED'}")
        print(f"Expected: {test['expected']}, Got: {result}")
