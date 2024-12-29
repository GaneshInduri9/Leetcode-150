"""
    Given the roots of two binary trees p and q, write a function to check
    if they are the same or not.Two binary trees are considered the same if
    they are structurally identical, and the nodes have the same value.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True 
        
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def test():
    s_obj = Solution()

    # Test 1: Identical trees
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    res = s_obj.isSameTree(p, q)
    print("Test 1 - Identical trees:", "same Tree" if res else "not a same Tree")

    # Test 2: Trees with different structure
    p = TreeNode(1, TreeNode(2), None)
    q = TreeNode(1, None, TreeNode(2))
    res = s_obj.isSameTree(p, q)
    print("Test 2 - Different structure:", "same Tree" if res else "not a same Tree")

    # Test 3: Trees with different values
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(4))
    res = s_obj.isSameTree(p, q)
    print("Test 3 - Different values:", "same Tree" if res else "not a same Tree")

    # Test 4: One tree is empty
    p = None
    q = TreeNode(1)
    res = s_obj.isSameTree(p, q)
    print("Test 4 - One tree is empty:", "same Tree" if res else "not a same Tree")

    # Test 5: Both trees are empty
    p = None
    q = None
    res = s_obj.isSameTree(p, q)
    print("Test 5 - Both trees are empty:", "same Tree" if res else "not a same Tree")

    # Test 6: Larger identical trees
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    res = s_obj.isSameTree(p, q)
    print("Test 6 - Larger identical trees:", "same Tree" if res else "not a same Tree")

    # Test 7: Larger trees with different values
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(8)))  # Different value at q.right.right
    res = s_obj.isSameTree(p, q)
    print("Test 7 - Larger trees with different values:", "same Tree" if res else "not a same Tree")

if __name__ == "__main__":
    test()

