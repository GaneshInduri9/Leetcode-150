"""
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.
"""
from typing import List
class Solution:
    # Brute Force
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dfs(i):
            if i >= n:
                return 0
            cost1 = dfs(i+1)+cost[i]
            cost2 = dfs(i+2)+cost[i]
            return min(cost1, cost2)
        return min(dfs(0), dfs(1))

    # Memo
    def minCostClimbingStairsMemo(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0
            cost1 = dfs(i+1)+cost[i]
            cost2 = dfs(i+2)+cost[i]
            memo[i] = min(cost1, cost2)
            return min(cost1, cost2)
        return min(dfs(0), dfs(1))

    
    def minCostClimbingStairsDp(self, cost: List[int]) -> int:
        n = len(cost)
        prev1, prev2 = 0, 0  # Initialize costs for the two steps ahead
        
        # Iterate from the second-to-last step to the first step
        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(prev1, prev2)  # Minimum cost from this step
            prev2 = prev1  # Update prev2 to be the cost of the next step
            prev1 = curr   # Update prev1 to be the current step's cost
        
        # Return the minimum cost starting from step 0 or step 1
        return min(prev1, prev2)

cost = [10, 15, 20]
solution = Solution()
print(solution.minCostClimbingStairs(cost))  # Output: 15 
