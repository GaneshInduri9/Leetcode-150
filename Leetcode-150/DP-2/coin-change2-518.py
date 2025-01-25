from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1 for _ in range(amount+1)] for i in range(n)]
        def f(i, T):
            if i == 0:
                if T % coins[i] == 0:
                    return 1
                else:
                    return 0
            if memo[i][T] != -1:
                return memo[i][T]
            notTake = 0 + f(i-1, T)
            take = 0
            if coins[i] <= T:
                take = f(i, T-coins[i])
            memo[i][T] = take + notTake
            return take + notTake
        return f(len(coins)-1, amount)
    
    def changeTab(self, amount: int, coins: List) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount +1 )] for _ in range(n)]

        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t]=1
        
        for i in range(1,n):
            for t in range(amount+1):
                notTake = 0 + dp[i-1][t]
                take = 0
                if coins[i] <= t:
                    take = dp[i][t-coins[i]]
                dp[i][t] = take + notTake
        
        return dp[n-1][amount]

    def changeSpace(self, amount: int, coins: List)-> int:
        n = len(coins)
        prev = [0]*(amount+1)
        for i in range(amount+1):
            if i % coins[0] == 0:
                prev[i] = 1
            
        for i in range(1,n):
            cur = [0]*(amount+1)
            for t in range(amount+1):
                notTake = 0 + prev[t]
                take = 0
                if coins[i] <= t:
                    take = cur[t-coins[i]]
                
                cur[t] = take + notTake
            prev = cur

        return prev[amount]


def test():
    sol = Solution()
    res = sol.change(5, [1,2,5])
    if res == 4:
        print("Test passed")
    else:
        print("Test failed")

    res1 = sol.changeTab(5, [1,2,5])
    if res1 == 4:
        print("Test passed")
    else:
        print("Test failed")
    
    res2 = sol.changeSpace(5, [1,2,5])
    if res2 == 4:
        print("Test passed")
    else:
        print("Test failed")

if __name__ == "__main__":
    test()
