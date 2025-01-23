"""
    Assume a theif wants to steal some money from a house and he has bunch of items and each item has a value
    and weight correspoding to that and also he has a bag of weight say capacity and also he can only pick each
    item once, now we wanna maximise the amount we can steal while not exceeding the capacity.
"""
from typing import List
class Solution:
    def knapsackMemo(self, val: List, wt: List, capacity: int) -> int:
        # code here
        n = len(val)
        memo = [[-1 for _ in range(capacity + 1)] for i in range(n)]
        def f(i, w):
            if i == 0:
                if wt[0] <= w:
                    return val[i]
                return 0
            if memo [i][w] != -1:
                return memo [i][w]
            notTake = 0 + f(i-1, w)
            take = 0
            if wt[i] <= w:
                take = val[i] + f(i-1, w-wt[i])
            memo [i][w] = max(take, notTake)
            return max(take, notTake)
        return f(n-1, capacity)
    
    def knapsackTab(self, val: List, wt: List, capacity: int) -> int:
        n = len(val)
        dp = [[0 for _ in range(capacity + 1)] for i in range(n)]
        for i in range(wt[0], capacity + 1):
            dp[0][i] = val[0]
        
        for i in range(1,n):
            for w in range(capacity + 1):
                notTake = 0 + dp[i-1][w]
                take = 0
                if wt[i] <= w:
                    take = val[i] + dp[i-1][w-wt[i]]
                
                dp[i][w] = max(notTake, take)
        return dp[n-1][w]

    def knapsackSpaceOptimized(self, val: List, wt: List, capacity: int) -> int:
        n = len(val)
        prev = [0 for _ in range(capacity + 1)]
        curr = [0 for _ in range(capacity + 1)]

        for w in range(wt[0], capacity +1):
            prev[w] = val[0]
        
        for i in range(1,n):
            for w in range(capacity + 1):
                notTake = 0 + prev[w]
                take = 0 
                if wt[i] <= w:
                    take = val[i] + prev[w - wt[i]]
                curr[i] = max(take, notTake)
            prev = curr
        
        return prev[capacity]

def main():
    sol = Solution()
    res = sol.knapsackMemo([40,30,50], [3,2,5], 5)
    print(res)

if __name__ == "__main__":
    main()