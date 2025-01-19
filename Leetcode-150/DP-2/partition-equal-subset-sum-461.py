from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sumn = sum(nums)
        if sumn % 2 != 0:
            return False

        half = sumn // 2

        def f(i, target):
            if target == 0:
                return True
            if i == 0:
                return nums[0] == target

            notTake = f(i - 1, target)
            take = False
            if nums[i] <= target:
                take = f(i - 1, target - nums[i])

            return take or notTake

        return f(len(nums) - 1, half)
    
    def canPartitionMemo(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sumn = sum(nums)
        if sumn % 2 != 0:
            return False

        half = sumn // 2
        n = len(nums)
        memo = [[-1 for _ in range(half + 1)] for _ in range(n)]

        def f(i, target):
            if target == 0:
                return True
            if i == 0:
                return nums[0] == target

            if memo[i][target] != -1:
                return memo[i][target]

            notTake = f(i - 1, target)
            take = False
            if nums[i] <= target:
                take = f(i - 1, target - nums[i])

            memo[i][target] = take or notTake
            return memo[i][target]

        return f(n - 1, half)
    
    def canPartitionTab(self, nums: List[int]) -> bool:
        if not nums:
            return False

        sumn = sum(nums)
        if sumn % 2 != 0:
            return False

        half = sumn // 2
        n = len(nums)
        dp = [[False for _ in range(half + 1)] for _ in range(n)]

        # Base cases
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= half:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for target in range(1, half + 1):
                notTake = dp[i - 1][target]
                take = False
                if nums[i] <= target:
                    take = dp[i - 1][target - nums[i]]
                dp[i][target] = take or notTake

        return dp[n - 1][half]

# Test function remains unchanged
def test_can_partition():
    solution = Solution()
    
    test_cases = [
        {
            "nums": [1, 5, 11, 5],
            "expected": True,
            "description": "Basic positive case",
        },
        {
            "nums": [1, 2, 3, 5],
            "expected": False,
            "description": "Basic negative case",
        },
        {
            "nums": [2, 2, 2, 2, 2, 2, 2, 2],
            "expected": True,
            "description": "Large equal numbers",
        },
        {
            "nums": [2],
            "expected": False,
            "description": "Single element case",
        },
        {
            "nums": [3, 3, 3, 3],
            "expected": True,
            "description": "All elements the same",
        },
        {
            "nums": [1, 1, 3],
            "expected": False,
            "description": "Odd total sum",
        },
        {
            "nums": [],
            "expected": False,
            "description": "Empty array",
        },
        {
            "nums": [1, 2, 5, 9, 7, 10],
            "expected": True,
            "description": "Larger array with possible partition",
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        nums = test["nums"]
        expected = test["expected"]
        description = test["description"]
        
        print(f"Test Case {i}: {description}")
        print(f"Input: {nums}")
        
        result_rec = solution.canPartition(nums)
        result_memo = solution.canPartitionMemo(nums)
        result_tab = solution.canPartitionTab(nums)
        
        print(f"Recursive Result: {result_rec}, Expected: {expected}")
        print(f"Memoization Result: {result_memo}, Expected: {expected}")
        print(f"Tabulation Result: {result_tab}, Expected: {expected}")
        
        assert result_rec == expected, f"Failed recursive test for {description}"
        assert result_memo == expected, f"Failed memoization test for {description}"
        assert result_tab == expected, f"Failed tabulation test for {description}"
        
        print(f"Test Case {i} passed!\n")

# Run the test function
test_can_partition()
