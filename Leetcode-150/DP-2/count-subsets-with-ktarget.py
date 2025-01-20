from typing import List
class Solution:
    def findWays(arr: List[int], k: int) -> int:
        n = len(arr)
        memo = [[-1 for _ in range(k+1)] for _ in range()]

        def f(i, cur):
            if cur == 0:
                return 1

            if  i == 0:
                if arr[i] == cur:
                    return 1
                return 0

            if memo[i][cur] != -1:
                return memo[i][cur]
            
            notTake = f(i-1, cur)
            take = 0
            if arr[i] <= cur:
                take = f(i-1, cur - arr[i])

            memo[i][cur] =  notTake + take
            return take + notTake
        return f(n-1, k)

    def findWaysTab(arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[0 for _ in range(k+1)] for _ in range()]

        for i in range(n):
            dp[i][0] = 1
        
        if arr[0] <= k:
            dp[0][arr[0]] = 1
        
        for i in range(1, n):
            for target in range(1,k+1):
                notTake = dp[i-1][target]
                take = 0
                if arr[i] <= target:
                    take = dp[i-1][target - arr[i]]
                
                dp[i][target] = take + notTake
        
        return dp[n-1][target]