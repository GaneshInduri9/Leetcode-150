class Solution:
    """
        The intuation behind this is the brute force way if we start at end i.e (m-1,n-1) how many ways we could
        move to above so here I have two choices I could move to one col above and I can row behind again from
        there I have two choices I could me to above or below so we can do this recursivly and find that there will
        be overlapping sub problems so solve that we can intialize memo so we dont repeat this problems.
    """
    def uniquePathsMemo(self, m: int, n: int) -> int:
        directions = [[-1, 0], [0, -1]]
        memo = {}
        def dfs(r,c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            res = 0
            for direction in directions:
                row, col = direction
                newR = r + row
                newC = c + col
                res += dfs(newR, newC)
            memo[(r,c)] = res
            return memo[(r,c)]

        return dfs(m-1,n-1)
    
    def uniquePathsTabulation(self, m: int, n: int) -> int:
        dp = [[0]*n]*m

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[m-1][n-1]
    
    def uniquePathsOptimal(self, m: int, n: int) -> int:
        prev = [0]*n

        for i in range(m):
            tmp = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    tmp[j] = 1
                    continue
                up =0 
                left = 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = tmp[j-1]
                
                tmp [j] = up + left
            prev = tmp
        
        return prev[n-1]
    
def test_unique_paths():
    solution = Solution()
    
    # Test case 1: Small grid
    assert solution.uniquePathsMemo(3, 2) == 3
    assert solution.uniquePathsTabulation(3, 2) == 3
    assert solution.uniquePathsOptimal(3, 2) == 3

    # Test case 2: Square grid
    assert solution.uniquePathsMemo(3, 3) == 6
    assert solution.uniquePathsTabulation(3, 3) == 6
    assert solution.uniquePathsOptimal(3, 3) == 6

    # Test case 3: Single row
    assert solution.uniquePathsMemo(1, 5) == 1
    assert solution.uniquePathsTabulation(1, 5) == 1
    assert solution.uniquePathsOptimal(1, 5) == 1

    # Test case 4: Single column
    assert solution.uniquePathsMemo(5, 1) == 1
    assert solution.uniquePathsTabulation(5, 1) == 1
    assert solution.uniquePathsOptimal(5, 1) == 1

    # Test case 5: Large grid
    assert solution.uniquePathsMemo(10, 10) == 48620
    assert solution.uniquePathsTabulation(10, 10) == 48620
    assert solution.uniquePathsOptimal(10, 10) == 48620

    # Test case 6: Edge case - smallest grid
    assert solution.uniquePathsMemo(1, 1) == 1
    assert solution.uniquePathsTabulation(1, 1) == 1
    assert solution.uniquePathsOptimal(1, 1) == 1

    print("All test cases passed!")

# Run the tests
test_unique_paths()

                




            
        