"""
    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # DFS APPROACH
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target = 0
        self.value = 0
        self.dfs(root, k)
        return self.value

    def dfs(self, root, k):
        if not root:
            return
        
        self.dfs(root.left, k)
        self.target += 1
        if self.target == k:
            self.value = root.val
            return
        self.dfs(root.right, k)

    # ITERATIVE APPROACH
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

# Test cases for kthSmallest and kthSmallestIterative

def test_kth_smallest():
    # Helper function to construct a binary tree
    def build_tree(values):
        if not values:
            return None
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = build_tree(values[:mid])
        root.right = build_tree(values[mid+1:])
        return root

    # Test Case 1: Simple BST
    # BST:       3
    #          /   \
    #         1     4
    #          \
    #           2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    
    sol = Solution()
    
    assert sol.kthSmallest(root, 1) == 1  # 1st smallest is 1
    assert sol.kthSmallest(root, 2) == 2  # 2nd smallest is 2
    assert sol.kthSmallest(root, 3) == 3  # 3rd smallest is 3
    assert sol.kthSmallest(root, 4) == 4  # 4th smallest is 4

    assert sol.kthSmallestIterative(root, 1) == 1  # Iterative test for 1st smallest
    assert sol.kthSmallestIterative(root, 2) == 2  # Iterative test for 2nd smallest
    assert sol.kthSmallestIterative(root, 3) == 3  # Iterative test for 3rd smallest
    assert sol.kthSmallestIterative(root, 4) == 4  # Iterative test for 4th smallest

    # Test Case 2: Larger BST
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = build_tree(values)  # Builds a balanced BST

    assert sol.kthSmallest(root, 1) == 1  # Smallest element
    assert sol.kthSmallest(root, 5) == 5  # Middle element
    assert sol.kthSmallest(root, 9) == 9  # Largest element

    assert sol.kthSmallestIterative(root, 1) == 1  # Iterative test for smallest
    assert sol.kthSmallestIterative(root, 5) == 5  # Iterative test for middle
    assert sol.kthSmallestIterative(root, 9) == 9  # Iterative test for largest

    # Test Case 3: Single Node Tree
    root = TreeNode(42)
    assert sol.kthSmallest(root, 1) == 42  # Only one element
    assert sol.kthSmallestIterative(root, 1) == 42  # Iterative test for single node

    # Test Case 4: Edge Case - Empty Tree
    root = None
    try:
        sol.kthSmallest(root, 1)
        assert False, "Expected an error for an empty tree"
    except:
        pass

    try:
        sol.kthSmallestIterative(root, 1)
        assert False, "Expected an error for an empty tree"
    except:
        pass

    print("All test cases passed!")

# Run the tests
test_kth_smallest()
