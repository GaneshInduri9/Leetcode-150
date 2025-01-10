""" 
    You are given an integer array nums where nums[i] represents the amount of 
    money the ith house has. The houses are arranged in a circle, i.e. the first 
    house and the last house are neighbors.You are planning to rob money from the houses,
    but you cannot rob two adjacent houses because the security system will 
    automatically alert the police if two adjacent houses were both broken into.
    Return the maximum amount of money you can rob without alerting the police.
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [[-1]*2 for _ in range(n)]
        def dfs(i, flag):

            if i >= n:
                return 0
            if i == n-1 and flag:
                return 0
            
            if memo[i][flag] !=-1:
                return memo[i][flag]
            
            skip = dfs(i+1, flag)
            rob = nums[i]+dfs(i+2,flag)
            memo[i][flag] = max(skip, rob)
            return memo[i][flag]
        

        rob_first = dfs(0,True)
        skip_first = dfs(1,False)
        return max(rob_first, skip_first)
    
    
    def robMemo(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag), 
                            nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))
    

    def robTab(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), 
                   self.helper(nums[:-1]))
    
    def helperTab(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]
    
    def robSpaceOptimized(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), 
                            self.helper(nums[:-1]))

    def helperSpaceOptimaized(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

def test_solution():
    sol = Solution()
    
    # Test Case 1: Single house
    assert sol.rob([5]) == 5, "Test Case 1 Failed"

    # Test Case 2: Two houses
    assert sol.rob([2, 3]) == 3, "Test Case 2 Failed"

    # Test Case 3: Three houses in a circle
    assert sol.rob([2, 3, 2]) == 3, "Test Case 3 Failed"

    # Test Case 4: Four houses
    assert sol.rob([1, 2, 3, 1]) == 4, "Test Case 4 Failed"

    # Test Case 5: Large number of houses
    assert sol.rob([6, 7, 1, 30, 8, 2, 4]) == 41, "Test Case 5 Failed"


    print("All test cases passed!")

test_solution()

