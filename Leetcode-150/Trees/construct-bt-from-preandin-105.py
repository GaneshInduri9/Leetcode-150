"""
    Given two integer arrays preorder and inorder where preorder is the preorder 
    traversal of a binary tree and inorder is the inorder traversal of the same tree, 
    construct and return the binary tree.
    Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
    Output: [1,2,3,null,null,null,4]
"""

from typing import Optional, List, Union
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
        The idea is to take advantage of the preorder elements and tree from 
        inorder. Preorder is structured in such a way that it has the root element 
        first, and if we find the root in inorder, the elements to the left of the root 
        index form the left subtree, and the elements to the right of the root index 
        form the right subtree. This is recursively true for every subtree since 
        inorder and preorder are built recursively.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preOrderIndex = 0
        n = len(inorder)
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return self.dfs(preorder, inorder_map, 0, n - 1)

    def dfs(self, preorder, inorder_map, left, right):
        if left > right:
            return None
        rootvalue = preorder[self.preOrderIndex]
        self.preOrderIndex += 1
        root = TreeNode(rootvalue)
        idx = inorder_map[rootvalue]
        root.left = self.dfs(preorder, inorder_map, left, idx - 1)
        root.right = self.dfs(preorder, inorder_map, idx + 1, right)
        return root 

# Helper function to serialize the binary tree into a list for comparison
def serialize(root: Optional[TreeNode]) -> List[Union[int, None]]:
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for clean output
    while result and result[-1] is None:
        result.pop()
    return result

# Test cases
def test_buildTree():
    sol = Solution()
    
    # Test Case 1
    preorder = [1, 2, 3, 4]
    inorder = [2, 1, 3, 4]
    expected = [1, 2, 3, None, None, None, 4]
    root = sol.buildTree(preorder, inorder)
    assert serialize(root) == expected, f"Test Case 1 Failed: {serialize(root)} != {expected}"
    
    # Test Case 2
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    expected = [3, 9, 20, None, None, 15, 7]
    root = sol.buildTree(preorder, inorder)
    assert serialize(root) == expected, f"Test Case 2 Failed: {serialize(root)} != {expected}"
    
    # Test Case 3
    preorder = [1]
    inorder = [1]
    expected = [1]
    root = sol.buildTree(preorder, inorder)
    assert serialize(root) == expected, f"Test Case 3 Failed: {serialize(root)} != {expected}"
    
    # Test Case 4
    preorder = []
    inorder = []
    expected = []
    root = sol.buildTree(preorder, inorder)
    assert serialize(root) == expected, f"Test Case 4 Failed: {serialize(root)} != {expected}"

    # Test Case 5
    preorder = [1, 2]
    inorder = [1, 2]
    expected = [1, None, 2]
    root = sol.buildTree(preorder, inorder)
    assert serialize(root) == expected, f"Test Case 5 Failed: {serialize(root)} != {expected}"

    print("All test cases passed!")

# Run the tests
test_buildTree()
