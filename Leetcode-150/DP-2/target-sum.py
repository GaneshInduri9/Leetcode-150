from typing import List
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def f(i, t):
            if i < 0:
                if t == 0:
                    return 1
                return 0

            if (i, t) in memo:
                return memo[(i,t)]

            plus = f(i-1, t + nums[i])
            minus = f(i-1, t - nums[i])
            memo[(i,t)] = plus + minus
            return plus + minus
        return f(n-1, target)
    
    def findTargetSumWaysTab(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]
