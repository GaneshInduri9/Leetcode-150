"""
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the
    chosen numbers sum to target. You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency
    of at least one of the chosen numbers is different.
    The test cases are generated such that the number of unique combinations that sum up to 
    target is less than 150 combinations for the given input.
"""
from typing import List
class Solution:
    """
        If we decide take one number in the decision we dont take that number again in the sub tree of desions. 
        Draw a deciosion Tree to understand this better.
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, currTotal, curr):
            if currTotal == target:
                res.append(curr.copy())
                return 

            if i>= n or currTotal > target:
                return
            
            # path where we include 2
            curr.append(nums[i])
            dfs(i, currTotal + nums[i], curr)
            #path where we don't include any 2 anymore
            curr.pop()
            dfs(i+1, currTotal, curr)

        dfs(0,0,[])
        return res
    
# Instantiate the Solution class
solution = Solution()

# Test case 1: Basic case
candidates = [2, 3, 6, 7]
target = 7
# Expected output: [[2, 2, 3], [7]]
print(solution.combinationSum(candidates, target))

# Test case 2: No possible combinations
candidates = [2, 4, 6]
target = 5
# Expected output: []
print(solution.combinationSum(candidates, target))

# Test case 3: Single candidate repeated to reach the target
candidates = [3]
target = 9
# Expected output: [[3, 3, 3]]
print(solution.combinationSum(candidates, target))

# Test case 4: Multiple candidates, small target
candidates = [2, 3, 5]
target = 8
# Expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(solution.combinationSum(candidates, target))

# Test case 5: Target is 0 (edge case)
candidates = [1, 2, 3]
target = 0
# Expected output: [[]] (empty combination to make target 0)
print(solution.combinationSum(candidates, target))

# Test case 6: Large numbers in candidates
candidates = [10, 20, 50]
target = 100
# Expected output: [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [50, 50]]
print(solution.combinationSum(candidates, target))

# Test case 7: Single element equal to the target
candidates = [5]
target = 5
# Expected output: [[5]]
print(solution.combinationSum(candidates, target))

# Test case 8: Duplicates in result should not appear
candidates = [2, 3]
target = 6
# Expected output: [[2, 2, 2], [3, 3]]
print(solution.combinationSum(candidates, target))
