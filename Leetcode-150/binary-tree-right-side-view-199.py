"""
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
"""
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        The only catch to this problem for not using dfs on right side of the tree
        is when what if the tree is not complete? Like what you would see from the right 
        isn't it the rightmost child of the left side?. So we are going to use 
        BFS to add the last child of every level so even if the tree is not complete 
        we know that the last element is going to be visible.

        Nice :)
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i+1 == size:
                    res.append(curr.val)
        return res

# Test cases
if __name__ == "__main__":
    # Test case 1: Perfect binary tree
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(Solution().rightSideView(root1))  # Expected: [1, 3, 7]

    # Test case 2: Tree with only left children
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    print(Solution().rightSideView(root2))  # Expected: [1, 2, 3, 4]

    # Test case 3: Tree with only right children
    root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(Solution().rightSideView(root3))  # Expected: [1, 2, 3, 4]

    # Test case 4: Tree with mixed children
    root4 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(Solution().rightSideView(root4))  # Expected: [1, 3, 4]

    # Test case 5: Single node tree
    root5 = TreeNode(1)
    print(Solution().rightSideView(root5))  # Expected: [1]

    # Test case 6: Empty tree
    root6 = None
    print(Solution().rightSideView(root6))  # Expected: []
