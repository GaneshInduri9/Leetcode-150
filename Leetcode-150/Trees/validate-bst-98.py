"""
    Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
    A valid binary search tree satisfies the following constraints:
    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        5
       / \
      1   4
         / \
        3   6
        for every element we pass a range saying that it should be bound in partcular range.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_value,max_value):
            if not node:
                return True
            
            if not (min_value < node.val < max_value):
                return False
            
            return dfs(node.left,min_value,node.val) and dfs(node.right,node.val,max_value)

        return dfs(root, float('-inf'), float('inf'))

# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def test_isValidBST():
    sol = Solution()

    # Test case 1: Valid BST
    root1 = build_tree([2, 1, 3])
    assert sol.isValidBST(root1) == True, "Test case 1 failed"

    # Test case 2: Invalid BST
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    assert sol.isValidBST(root2) == False, "Test case 2 failed"

    # Test case 3: Single-node tree (valid BST)
    root3 = build_tree([1])
    assert sol.isValidBST(root3) == True, "Test case 3 failed"

    # Test case 4: Empty tree (valid BST)
    root4 = build_tree([])
    assert sol.isValidBST(root4) == True, "Test case 4 failed"

    # Test case 5: Larger valid BST
    root5 = build_tree([10, 5, 15, None, None, 12, 20])
    assert sol.isValidBST(root5) == True, "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_isValidBST()