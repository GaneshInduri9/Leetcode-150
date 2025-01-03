"""
    Given a binary tree, return true if it is height-balanced and false otherwise.
    A height-balanced binary tree is defined as a binary tree in which the left and
    right subtrees of every node differ in height by no more than 1.
    Input: root = [1,2,3,null,null,4]
    Output: true
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        if res == -1:
            return False
        return True

    def dfs(self, root):
        if root is None:
            return 0
        
        leftHeight = self.dfs(root.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.dfs(root.right)
        if rightHeight == -1:
            return -1

        balance = abs(leftHeight - rightHeight)
        if balance > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)

# Test cases
def test_isBalanced():
    sol = Solution()

    # Test case 1: Balanced tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isBalanced(root) == True, "Test case 1 failed"

    # Test case 2: Unbalanced tree
    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    assert sol.isBalanced(root) == False, "Test case 2 failed"

    # Test case 3: Empty tree
    root = None
    assert sol.isBalanced(root) == True, "Test case 3 failed"

    # Test case 4: Single node tree
    root = TreeNode(1)
    assert sol.isBalanced(root) == True, "Test case 4 failed"

    # Test case 5: Balanced tree with multiple levels
    root = TreeNode(1, 
                    TreeNode(2, TreeNode(4), TreeNode(5)), 
                    TreeNode(3, None, TreeNode(6)))
    assert sol.isBalanced(root) == True, "Test case 5 failed"

    # Test case 6: Deeply unbalanced tree
    root = TreeNode(1, 
                    TreeNode(2, 
                             TreeNode(3, 
                                      TreeNode(4), None)), None)
    assert sol.isBalanced(root) == False, "Test case 6 failed"

    print("All test cases passed!")

# Run tests
test_isBalanced()