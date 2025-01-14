from typing import List
class Solution:
    """
        Pre : Need to solve the previous problem uniquePaths
        It's the same as uniquePaths we have 2 choices at every index 
        # we can go above or side (left) so lets just try out all 
        ways see how many ways we could reach the end.
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(r,c):
            # base 1 
            if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
                return 0
            # base 2
            if r == 0 and c == 0:
                return 1
            
            
            up = dfs(r-1, c)
            left = dfs(r, c-1)
            return up + left
        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
    
    def uniquePathsWithObstaclesMemo(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        def dfs(r,c):
            # base 1 
            if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
                return 0
            # base 2
            if r == 0 and c == 0:
                return 1

            # base 3
            if (r,c) in memo:
                return memo[(r,c)]
            
            
            up = dfs(r-1, c)
            left = dfs(r, c-1)
            memo[(r,c)] = up + left
            return up + left
        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
    
    def uniquePathsWithObstaclesTabulation(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []

        for i in range(m):
            dp.append([0]*n)
        
        for i in range(m):
            for j  in range(n):
                if i == 0 and j == 0:
                    # Make sure it's not an obstacle in begining only
                    dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                    continue;
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue;
                else:
                    up = 0 
                    left = 0

                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        left = dp[i][j-1]
                    dp[i][j] = left + up
        
        return dp[m-1][n-1]

    def uniquePaths(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n

        for i in range(m):
            tmp = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    tmp[j] = 0  # If there is an obstacle, set paths to 0
                    continue
                if i == 0 and j == 0:
                    tmp[j] = 1  # Start point, set paths to 1
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = prev[j]  # Number of paths from the row above
                if j > 0:
                    left = tmp[j - 1]  # Number of paths from the column to the left
                tmp[j] = up + left  # Total paths to this cell
            prev = tmp  # Update the previous row for the next iteration

        return prev[n - 1]  # Return the result in the bottom-right corner

def test_unique_paths_with_obstacles():
    solution = Solution()
    
    # Test Case 1: Basic Grid without Obstacles
    obstacleGrid1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Expected Output: 6 paths (2 choices at each step)
    assert solution.uniquePathsWithObstacles(obstacleGrid1) == 6
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid1) == 6
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid1) == 6
    assert solution.uniquePaths(obstacleGrid1) == 6
    
    # Test Case 2: Grid with Obstacles
    obstacleGrid2 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]
    # Expected Output: 2 paths (one path is blocked by obstacles)
    assert solution.uniquePathsWithObstacles(obstacleGrid2) == 2
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid2) == 2
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid2) == 2
    assert solution.uniquePaths(obstacleGrid2) == 2
    
    # Test Case 3: Starting or Ending Cell is Blocked
    obstacleGrid3 = [
        [1, 0],
        [0, 0]
    ]
    # Expected Output: 0 paths (start point is blocked)
    assert solution.uniquePathsWithObstacles(obstacleGrid3) == 0
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid3) == 0
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid3) == 0
    assert solution.uniquePaths(obstacleGrid3) == 0
    
    # Test Case 4: Single Row Grid with Obstacles
    obstacleGrid4 = [
        [0, 1, 0, 0, 0]
    ]
    # Expected Output: 1 path (can only move right)
    assert solution.uniquePathsWithObstacles(obstacleGrid4) == 1
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid4) == 1
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid4) == 1
    assert solution.uniquePaths(obstacleGrid4) == 1
    
    # Test Case 5: Single Column Grid with Obstacles
    obstacleGrid5 = [
        [0],
        [1],
        [0]
    ]
    # Expected Output: 0 paths (blocked in the middle)
    assert solution.uniquePathsWithObstacles(obstacleGrid5) == 0
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid5) == 0
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid5) == 0
    assert solution.uniquePaths(obstacleGrid5) == 0
    
    # Test Case 6: 1x1 Grid with Obstacle
    obstacleGrid6 = [
        [1]
    ]
    # Expected Output: 0 paths (starting point is blocked)
    assert solution.uniquePathsWithObstacles(obstacleGrid6) == 0
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid6) == 0
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid6) == 0
    assert solution.uniquePaths(obstacleGrid6) == 0
    
    # Test Case 7: Grid with Obstacles along the Path
    obstacleGrid7 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # Expected Output: 2 paths (blocked in the middle row)
    assert solution.uniquePathsWithObstacles(obstacleGrid7) == 2
    assert solution.uniquePathsWithObstaclesMemo(obstacleGrid7) == 2
    assert solution.uniquePathsWithObstaclesTabulation(obstacleGrid7) == 2
    assert solution.uniquePaths(obstacleGrid7) == 2
    
    print("All test cases passed!")

test_unique_paths_with_obstacles()

