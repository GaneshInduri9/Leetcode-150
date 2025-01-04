""" 
    Given an integer array nums that may contain duplicates, return all possible 
    subsets(the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    Input: nums = [1,2,1]
    Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
"""
from typing import List
class Solution:

    """
        Draw a desision tree and see where the duplicates are branched.
        sorting helps in removing the dups.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        n = len(nums)
        def dfs(i):
            if i >= n:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            while i+1<n and nums[i] == nums[i+1]:
                i += 1
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

def test_subsets_with_dup():
    solution = Solution()

    # Test Case 1: Example in the prompt
    nums = [1, 2, 1]
    expected = [[], [1], [1, 1], [1, 2], [1, 2, 1], [2]]
    assert sorted(map(sorted, solution.subsetsWithDup(nums))) == sorted(map(sorted, expected)), "Test Case 1 Failed"

    # Test Case 2: No duplicates
    nums = [1, 2, 3]
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(map(sorted, solution.subsetsWithDup(nums))) == sorted(map(sorted, expected)), "Test Case 2 Failed"

    # Test Case 3: All elements are duplicates
    nums = [2, 2, 2]
    expected = [[], [2], [2, 2], [2, 2, 2]]
    assert sorted(map(sorted, solution.subsetsWithDup(nums))) == sorted(map(sorted, expected)), "Test Case 3 Failed"

    # Test Case 4: Empty input
    nums = []
    expected = [[]]
    assert solution.subsetsWithDup(nums) == expected, "Test Case 4 Failed"

    # Test Case 7: Large input with duplicates
    nums = [1, 2, 2, 3]
    # The number of unique subsets is 2^number of distinct elements
    result = solution.subsetsWithDup(nums)
    assert len(result) == len(set(tuple(sorted(sub)) for sub in result)), "Test Case 7 Failed (Duplicates Exist)"

    print("All test cases passed!")

# Run the tests
test_subsets_with_dup()
