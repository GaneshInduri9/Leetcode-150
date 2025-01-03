"""
    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.
"""
from typing import List
class Solution:
    """ 
        Draw a desision tree we find out that it leads to some duplicate combinations to avoid this sort
        the input and ingnore the same numbers that way when comeing from back track we avoid duplicates.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, currTotal, curr):
            if currTotal == target:
                res.append(curr.copy())
                return
            if i >= n or currTotal > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, currTotal+ candidates[i], curr)

            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            
            curr.pop()
            dfs(i + 1, currTotal, curr)

        dfs(0, 0, [])
        return res
    
# Test cases for the Solution
solution = Solution()

# Test Case 1: General case with duplicates in input
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print("Test Case 1:", solution.combinationSum2(candidates, target))
# Expected Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]] (Order may vary)

# Test Case 2: No solution possible
candidates = [2, 4, 6]
target = 5
print("Test Case 2:", solution.combinationSum2(candidates, target))
# Expected Output: []

# Test Case 3: Single element equals target
candidates = [3]
target = 3
print("Test Case 3:", solution.combinationSum2(candidates, target))
# Expected Output: [[3]]

# Test Case 4: Single element less than target
candidates = [3]
target = 4
print("Test Case 4:", solution.combinationSum2(candidates, target))
# Expected Output: []

# Test Case 5: All elements equal target
candidates = [5, 5, 5]
target = 5
print("Test Case 5:", solution.combinationSum2(candidates, target))
# Expected Output: [[5]]

# Test Case 6: Multiple elements but only one valid combination
candidates = [2, 3, 6, 7]
target = 7
print("Test Case 6:", solution.combinationSum2(candidates, target))
# Expected Output: [[7]]

# Test Case 7: Large input with duplicates
candidates = [1, 1, 2, 2, 2, 5]
target = 5
print("Test Case 7:", solution.combinationSum2(candidates, target))
# Expected Output: [[1, 1, 2, 2], [2, 2, 1], [5]] (Order and structure may vary based on implementation)

# Test Case 8: Empty input
candidates = []
target = 7
print("Test Case 8:", solution.combinationSum2(candidates, target))
# Expected Output: []

# Test Case 9: Target is 0
candidates = [1, 2, 3]
target = 0
print("Test Case 9:", solution.combinationSum2(candidates, target))
# Expected Output: []
