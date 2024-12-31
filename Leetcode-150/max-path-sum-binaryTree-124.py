"""
    Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has
    an edge connecting them. A node can not appear in the sequence more than once. The path does
    not necessarily need to include the root.
"""

from typing import Optional, Union, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
        Key note: in a path, we don't visit each node twice.
        We compute two things for each node:
        1. If we take a split at this node, what's the maximum path sum? 
           If this maximum path sum is greater than our previous max sum, we update it.
        2. If we don't take a split, what's the maximum path sum for this node? 
           It is calculated as root.val + max(left_max_path_sum, right_max_path_sum), 
           and this value is returned to the parent node.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # Ignore negative paths as they don't contribute to the max sum
            left_max = max(0, left_max)
            right_max = max(0, right_max)

            # Update the maximum path sum if the current path (split at root) is larger
            res[0] = max(res[0], root.val + left_max + right_max)

            # Return the max path sum for the current node without split
            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]

# Helper function to build a binary tree from a list
def build_tree(values: List[Union[int, None]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if current:
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
    return root

# Test cases
def test_maxPathSum():
    sol = Solution()

    # Test Case 1: General case
    tree = build_tree([-10, 9, 20, None, None, 15, 7])
    expected = 42  # The path is 15 -> 20 -> 7
    assert sol.maxPathSum(tree) == expected, f"Test Case 1 Failed: {sol.maxPathSum(tree)} != {expected}"

    # Test Case 2: Single node tree
    tree = build_tree([1])
    expected = 1
    assert sol.maxPathSum(tree) == expected, f"Test Case 2 Failed: {sol.maxPathSum(tree)} != {expected}"

    # Test Case 3: Linear tree with negative values
    tree = build_tree([1, 2, 3])
    expected = 6  # The path is 1 -> 2 -> 3
    assert sol.maxPathSum(tree) == expected, f"Test Case 3 Failed: {sol.maxPathSum(tree)} != {expected}"

    # Test Case 4: Mixed positive and negative values
    tree = build_tree([10, 2, 10, 20, 1, -25, None, None, None, None, None, 3, 4])
    expected = 42  # The path is 20 -> 2 -> 10 -> 10
    assert sol.maxPathSum(tree) == expected, f"Test Case 4 Failed: {sol.maxPathSum(tree)} != {expected}"

    # Test Case 5: All negative values
    tree = build_tree([-3, -2, -1])
    expected = -1  # The path is -1
    assert sol.maxPathSum(tree) == expected, f"Test Case 5 Failed: {sol.maxPathSum(tree)} != {expected}"

    print("All test cases passed!")

# Run the tests
test_maxPathSum()
