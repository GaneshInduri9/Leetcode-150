"""
    Given an integer array nums of unique elements, return all possible subsets
    (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List
class Solution:
    """
        The decision Tree will have two at every level we can take that number other wise we don't
        once the decision Tree is drawn problem is easy
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def dfs(i):
            if i>= n:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


def test_subsets():
    solution = Solution()
    
    # Test 1: Basic test case with a small array
    nums1 = [1, 2, 3]
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result1 = solution.subsets(nums1)
    print(f"Test 1 - Expected: {expected1}, Got: {result1}")
    assert sorted(result1) == sorted(expected1), "Test 1 Failed"

    # Test 2: Test with a single element
    nums2 = [1]
    expected2 = [[], [1]]
    result2 = solution.subsets(nums2)
    print(f"Test 2 - Expected: {expected2}, Got: {result2}")
    assert sorted(result2) == sorted(expected2), "Test 2 Failed"

    # Test 3: Test with multiple elements (more than 2)
    nums3 = [0, 1]
    expected3 = [[], [0], [1], [0, 1]]
    result3 = solution.subsets(nums3)
    print(f"Test 3 - Expected: {expected3}, Got: {result3}")
    assert sorted(result3) == sorted(expected3), "Test 3 Failed"

    # Test 4: Test with larger input
    nums4 = [1, 2, 3, 4]
    expected4 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
    result4 = solution.subsets(nums4)
    print(f"Test 4 - Expected: {expected4}, Got: {result4}")
    assert sorted(result4) == sorted(expected4), "Test 4 Failed"

    # Test 5: Edge case with an empty array
    nums5 = []
    expected5 = [[]]
    result5 = solution.subsets(nums5)
    print(f"Test 5 - Expected: {expected5}, Got: {result5}")
    assert result5 == expected5, "Test 5 Failed"

    print("All tests passed!")

# Run the tests
test_subsets()
