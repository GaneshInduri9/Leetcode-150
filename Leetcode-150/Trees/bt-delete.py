# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)

        curr = root
        while curr:
            if key < curr.val:

                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                else:
                    curr = curr.right
        return root

    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        right_child = root.right
        left_max_child = self.findright(root.left)
        left_max_child.right = right_child
        return root.left

    def findright(self, root):
        if root.right is None:
            return root
        return self.findright(root.right)
