"""
    Given the root of a binary tree, return the level order traversal of its nodes'
    values. (i.e., from left to right, level by level).

    Input: root = [1,2,3,4,5,6,7]
    Output: [[1],[2,3],[4,5,6,7]]
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
        The only tricky part of this problem is how are we going to know
        the size of each level. Simply, we can take the size of the queue
        and pop that many elements while also adding the left and right 
        children of those nodes to the queue. The inner loop only runs until 
        the size of each level.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            curr_list = []

            for i in range(size):
                curr = q.popleft()
                curr_list.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr_list)
        return res

# Tests
if __name__ == "__main__":
    # Test case 1: Perfect binary tree
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(Solution().levelOrder(root1))  # Expected: [[1], [2, 3], [4, 5, 6, 7]]

    # Test case 2: Single node tree
    root2 = TreeNode(1)
    print(Solution().levelOrder(root2))  # Expected: [[1]]

    # Test case 3: Tree with only left children
    root3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    print(Solution().levelOrder(root3))  # Expected: [[1], [2], [3], [4]]

    # Test case 4: Tree with only right children
    root4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(Solution().levelOrder(root4))  # Expected: [[1], [2], [3], [4]]

    # Test case 5: Empty tree
    root5 = None
    print(Solution().levelOrder(root5))  # Expected: []

    # Test case 6: Mixed tree
    root6 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(Solution().levelOrder(root6))  # Expected: [[1], [2, 3], [4, 5]]
