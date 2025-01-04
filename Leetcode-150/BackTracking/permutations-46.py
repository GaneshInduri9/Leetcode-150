"""
    Given an array nums of distinct integers, return all the possible permutations
    You can return the answer in any order.

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution:
    """
        The idea is solve the sub problem first draw decision tree [1,2,3] will understand better
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutaions = self.permute(nums[1:])
        res = []
        for p in permutaions:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res
    
    """ The same approach as above nothing changes much we start at the base case and place at every position"""
    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        
        return perms
                    
def test_permutations():
    solution = Solution()

    # Test Case 1: Example in the prompt
    nums = [1, 2, 3]
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1]
    ]
    assert sorted(solution.permute(nums)) == sorted(expected), "Test Case 1 Failed"
    assert sorted(solution.permuteIterative(nums)) == sorted(expected), "Test Case 1 Iterative Failed"

    # Test Case 2: Single element
    nums = [5]
    expected = [[5]]
    assert solution.permute(nums) == expected, "Test Case 2 Failed"
    assert solution.permuteIterative(nums) == expected, "Test Case 2 Iterative Failed"

    # Test Case 3: Two elements
    nums = [1, 2]
    expected = [[1, 2], [2, 1]]
    assert sorted(solution.permute(nums)) == sorted(expected), "Test Case 3 Failed"
    assert sorted(solution.permuteIterative(nums)) == sorted(expected), "Test Case 3 Iterative Failed"

    # Test Case 4: Empty list
    nums = []
    expected = [[]]
    assert solution.permute(nums) == expected, "Test Case 4 Failed"
    assert solution.permuteIterative(nums) == expected, "Test Case 4 Iterative Failed"

    # Test Case 5: Larger input
    nums = [1, 2, 3, 4]
    # The number of permutations for 4 elements is 4! = 24
    result_recursive = solution.permute(nums)
    result_iterative = solution.permuteIterative(nums)
    assert len(result_recursive) == 24, "Test Case 5 Failed (Recursive Length)"
    assert len(result_iterative) == 24, "Test Case 5 Failed (Iterative Length)"
    assert sorted(result_recursive) == sorted(result_iterative), "Test Case 5 Failed (Results Mismatch)"

    print("All test cases passed!")

# Run the tests
test_permutations()
