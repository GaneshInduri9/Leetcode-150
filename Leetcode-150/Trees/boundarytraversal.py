from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isLeafNode(self, curr: TreeNode) -> bool:
        if not curr.left and not curr.right:
            return True
        return False

    def boundary_traversal(self, root: TreeNode) -> List[int]:

        output = []
        if not root:
            return output

        output.append(root.val)
        # left
        self.add_left_boundary(root.left, output)
        # leaf
        self.add_leaf_nodes(root.right, output)

        # right revrese
        res = self.add_right(root)
        while res:
            output.append(res.pop())

        return output

    def add_left_boundary(self, curr: TreeNode, output: List[int]) -> None:

        while curr:
            if self.isLeafNode(curr):
                return
            output.append(curr.val)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def add_leaf_nodes(self, curr: TreeNode, output: List[int]) -> None:
        if self.isLeafNode(curr):
            output.append(curr.val)

        self.add_leaf_nodes(curr.left)
        self.add_leaf_nodes(curr.right)

    def add_right(self, curr: TreeNode) -> List[int]:
        res = []
        while curr:
            if self.isLeafNode(curr):
                return
            res.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        return res
