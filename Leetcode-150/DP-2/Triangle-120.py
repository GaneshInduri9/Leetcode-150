
from typing import List
class Solution:
    "This approach is not optimal for even brute force as"
    def minimumTotalFromBottom(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            # reached start from end
            if i== 0 and j == 0:
                return triangle[0][0]

            if i < 0 or j < 0 or j >= len(triangle[i]):  # Out of bounds
                return float('inf')
            
            above  = triangle[i][j] + dfs(i-1, j)
            diag = triangle [i][j] + dfs(i-1, j-1)

            return min(above, diag)
        n = len(triangle) 
        minv = float('inf')           
        for i in range(n-1, -1,-1):
            minv = min(dfs(n-1,i), minv)
        return minv

    def minimumTotalFromStart(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def dfs(i, j):
            # When we reach last row we could return the res
            if i== n-1:
                return triangle[i][j]
            
            below  = triangle[i][j] + dfs(i+1, j)
            diag = triangle [i][j] + dfs(i+1, j+1)
            return min(below, diag)
        return dfs(0,0)
    
    def minimumTotalFromTab(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(n)] for i in range(n)]

        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                below = triangle[i][j] + dp[i+1][j]
                diag = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(below, diag)
        
        return dp[0][0]
def test_solution():
    sol = Solution()
    
    # Test case 1: Single element triangle
    triangle1 = [[2]]
    assert sol.minimumTotalFromBottom(triangle1) == 2
    assert sol.minimumTotalFromStart(triangle1) == 2
    assert sol.minimumTotalFromTab(triangle1) == 2

    # Test case 2: Small triangle
    triangle2 = [
        [2],
        [3, 4],
        [6, 5, 7]
    ]
    assert sol.minimumTotalFromBottom(triangle2) == 10  # Path: 2 -> 3 -> 5
    assert sol.minimumTotalFromStart(triangle2) == 10
    assert sol.minimumTotalFromTab(triangle2) == 10

    # Test case 3: Medium-sized triangle
    triangle3 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    assert sol.minimumTotalFromBottom(triangle3) == 11  # Path: 2 -> 3 -> 5 -> 1
    assert sol.minimumTotalFromStart(triangle3) == 11
    assert sol.minimumTotalFromTab(triangle3) == 11

    # Test case 4: Larger triangle
    triangle4 = [
        [5],
        [9, 6],
        [4, 6, 8],
        [0, 7, 1, 5]
    ]
    print(sol.minimumTotalFromBottom(triangle4))
    assert sol.minimumTotalFromBottom(triangle4) == 18  # Path: 5 -> 6 -> 6 -> 1
    assert sol.minimumTotalFromStart(triangle4) == 18
    assert sol.minimumTotalFromTab(triangle4) == 18

    # Test case 5: Negative numbers
    triangle5 = [
        [-1],
        [2, 3],
        [1, -1, -3]
    ]
    assert sol.minimumTotalFromBottom(triangle5) == -1  # Path: -1 -> 3 -> -3
    assert sol.minimumTotalFromStart(triangle5) == -1
    assert sol.minimumTotalFromTab(triangle5) == -1

    # Test case 6: Edge case with all zeros
    triangle6 = [
        [0],
        [0, 0],
        [0, 0, 0]
    ]
    assert sol.minimumTotalFromBottom(triangle6) == 0
    assert sol.minimumTotalFromStart(triangle6) == 0
    assert sol.minimumTotalFromTab(triangle6) == 0

    print("All test cases passed!")

# Run the tests
test_solution()
