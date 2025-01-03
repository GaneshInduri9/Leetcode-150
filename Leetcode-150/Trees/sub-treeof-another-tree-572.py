"""
    Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root with the same 
    structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of
    node in tree and all of this node's descendants. The tree tree 
    could also be considered as a subtree of itself.
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False  # If the main tree is empty, return False immediately.
        
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()

            # Check if the current node matches the subtree
            if self.isSameTree(curr, subRoot):
                return True

            # Continue traversing the tree using BFS
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            
        return False
    
    def isSubtreeDFS(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # Check if current root matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        # If both are None, trees are identical
        if not p and not q:
            return True
        # If one is None and the other is not, they are not identical
        if not p or not q:
            return False
        # Compare the values of the current nodes
        if p.val != q.val:
            return False
        # Recursively check left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test():
    s = Solution()

    # Test case 1: subRoot is a subtree of root
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(0)

    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)

    assert s.isSubtree(root1, subRoot1) == True, "Test Case 1 Failed"

    # Test case 2: subRoot is not a subtree of root
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)

    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(3)  # Different right child

    assert s.isSubtree(root2, subRoot2) == False, "Test Case 2 Failed"

    # Test case 3: root is empty, subRoot is not empty
    root3 = None
    subRoot3 = TreeNode(1)
    assert s.isSubtree(root3, subRoot3) == False, "Test Case 3 Failed"

    # Test case 4: subRoot is empty, root is not empty
    root4 = TreeNode(1)
    subRoot4 = None
    assert s.isSubtree(root4, subRoot4) == False, "Test Case 4 Failed"

    # Test case 5: root and subRoot are both empty
    root5 = None
    subRoot5 = None
    assert s.isSubtree(root5, subRoot5) == True, "Test Case 5 Failed"

    # Test case 6: root is a subtree of itself
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)

    assert s.isSubtree(root6, root6) == True, "Test Case 6 Failed"

    print("All test cases passed!")

# Run the tests
test()

if __name__ == "__main__":
    test()
