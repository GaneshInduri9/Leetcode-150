# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_node = None
        parent = {}
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.val == start:
                start_node = curr

            if curr.left:
                parent[curr.left] = curr
                q.append(curr.left)

            if curr.right:
                parent[curr.right] = curr
                q.append(curr.right)

        q.append((start_node, 0))
        time = 0
        v = set()
        v.add(start_node)
        while q:
            curr, t = q.popleft()
            time = max(t, time)

            if curr.left and curr.left not in v:
                v.add(curr.left)
                q.append((curr.left, t + 1))

            if curr.right and curr.right not in v:
                v.add(curr.right)
                q.append((curr.right, t + 1))

            if parent.get(curr) and parent[curr] not in v:
                v.add(parent[curr])
                q.append((parent[curr], t + 1))
        return time
