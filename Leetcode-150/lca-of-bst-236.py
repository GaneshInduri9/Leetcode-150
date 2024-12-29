"""
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
    between two nodes p and q as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    "The key idea is to observe that the point they become divergent becomes the lowest common ancestor"
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    def lowestCommonAncestorOptimal(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        return None

# Test cases
if __name__ == "__main__":
    # Build a sample binary search tree
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    solution = Solution()

    # Test case 1: LCA of 2 and 8
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 6
    print(solution.lowestCommonAncestorOptimal(root, p, q).val)  # Output: 6

    # Test case 2: LCA of 2 and 4
    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 2
    print(solution.lowestCommonAncestorOptimal(root, p, q).val)  # Output: 2

    # Test case 3: LCA of 3 and 5
    p = root.left.right.left  # Node with value 3
    q = root.left.right.right  # Node with value 5
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 4
    print(solution.lowestCommonAncestorOptimal(root, p, q).val)  # Output: 4

    # Test case 4: LCA of 7 and 9
    p = root.right.left  # Node with value 7
    q = root.right.right  # Node with value 9
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 8
    print(solution.lowestCommonAncestorOptimal(root, p, q).val)  # Output: 8
