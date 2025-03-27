class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def dfs(node):

            if not node:
                return 0

            if not node.left and not node.right:
                return node.data

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            total = left + right
            if total == node.data:
                return node.data
            else:
                return -1

        res = dfs(root)
        if res >= 0:
            return 1
        return 0
