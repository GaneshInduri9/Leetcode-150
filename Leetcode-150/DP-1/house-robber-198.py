"""
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint 
    stopping you from robbing each of them is that adjacent houses have 
    security systems connected and it will automatically contact the police if 
    two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
"""
from typing import List
class Solution:
    """
        At every step we have 2 choices either we can pick current or not pick current
        so we can skip the current house and take the i+2 house because we can't take the
        next imediate house. Our max will if start at 0 house 1 house.
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            skip = dfs(i+1)
            rob = nums[i] + dfs(i+2)
            memo[i] = max(skip, rob)
            return memo[i]
        return dfs(0)

    def robTabulation(self, nums: List[int]) -> int:
        n = len(nums)
        spSize = n+3
        dp = [0]*spSize

        for i in range(n-1,-1,-1):
            dp[i]= nums[i] + max(dp[i+2],dp[i+3])
        return max(dp[0],dp[1])
    
    def robOptimal(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for n in nums:
            curr = max(prev1, n+prev2)
            prev2 = prev1
            prev1 = curr
        return prev1

# Test cases
def test_rob_methods():
    solution = Solution()

    # Test case 1: Basic input with no adjacent houses being robbed
    nums1 = [1, 2, 3, 1]
    print("Test Case 1:")
    print(solution.rob(nums1))             # Expected: 4
    print(solution.robTabulation(nums1))  # Expected: 4
    print(solution.robOptimal(nums1))     # Expected: 4

    # Test case 2: All houses have the same amount
    nums2 = [10, 10, 10, 10, 10]
    print("\nTest Case 2:")
    print(solution.rob(nums2))             # Expected: 30
    print(solution.robTabulation(nums2))  # Expected: 30
    print(solution.robOptimal(nums2))     # Expected: 30

    # Test case 3: Single house
    nums3 = [100]
    print("\nTest Case 3:")
    print(solution.rob(nums3))             # Expected: 100
    print(solution.robTabulation(nums3))  # Expected: 100
    print(solution.robOptimal(nums3))     # Expected: 100

    # Test case 4: Two houses
    nums4 = [20, 30]
    print("\nTest Case 4:")
    print(solution.rob(nums4))             # Expected: 30
    print(solution.robTabulation(nums4))  # Expected: 30
    print(solution.robOptimal(nums4))     # Expected: 30

    # Test case 5: Alternating high and low values
    nums5 = [2, 7, 9, 3, 1]
    print("\nTest Case 5:")
    print(solution.rob(nums5))             # Expected: 12
    print(solution.robTabulation(nums5))  # Expected: 12
    print(solution.robOptimal(nums5))     # Expected: 12

    # Test case 6: All values are zero
    nums6 = [0, 0, 0, 0]
    print("\nTest Case 6:")
    print(solution.rob(nums6))             # Expected: 0
    print(solution.robTabulation(nums6))  # Expected: 0
    print(solution.robOptimal(nums6))     # Expected: 0

    # Test case 7: Large input array
    nums7 = [10] * 1000  # All houses have 10
    print("\nTest Case 7:")
    print(solution.rob(nums7))             # Expected: 5000
    print(solution.robTabulation(nums7))  # Expected: 5000
    print(solution.robOptimal(nums7))     # Expected: 5000

    # Test case 8: Edge case, empty array
    nums8 = []
    print("\nTest Case 8:")
    print(solution.rob(nums8))             # Expected: 0
    print(solution.robTabulation(nums8))  # Expected: 0
    print(solution.robOptimal(nums8))     # Expected: 0

# Run tests
test_rob_methods()





