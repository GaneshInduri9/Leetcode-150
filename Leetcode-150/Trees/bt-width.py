# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        max_width = 1

        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                node, n = cur
                if node.left:
                    q.append((node.left, (2 * n)))
                if node.right:
                    q.append((node.right, (2 * n + 1)))
            if len(q) >= 2:
                first = q[0]
                last = q[-1]

                left, li = first
                right, ri = last
                max_width = max(max_width, ri - li + 1)

        return max_width
