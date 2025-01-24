from typing import List
class Solution:
    def findMinWays(self, coins: List, target: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(target+1)] for _ in range(n)]
        def f(i, t):
            if i == 0:
                if t % coins[i] == 0:
                    return t // coins[0]
                return int(1e9)
            if dp[i][t] != -1:
                return dp[i][t]
            notTake = 0 + f(i-1, t)
            take = int(1e9)
            if coins[i] <= t:
                take = 1 + f(i, t-coins[i])
            dp[i][t] = min(take, notTake)
            return min(take, notTake)
        res =  f(n-1, target)
        if res == int(1e9):
            return -1
        return res
    
    def findMinWaysTab(self, coins: List, target: int) -> int:
        n = len(coins)
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]

        for t in range(target + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]
            else :
                dp[0][t] = int(1e9)
            
        
        for i in range(1, n):
            for t in range(target+1):
                notTake = 0 + dp[i-1][t]

                take = int(1e9)
                if coins[i] <= t:
                    take = 1 + dp[i][t - coins[i]]
                
                dp[i][t] = min(take, notTake)
            
        res = dp[n-1][target]
        if res == int(1e9):
            return -1
        return res

def test_find_min_ways():
    sol = Solution()
    res = sol.findMinWays([1,2,3], 7)
    print(res)
    res1 = sol.findMinWaysTab([1,2,3], 7)
    print(res1)

if __name__ == "__main__":
    test_find_min_ways()