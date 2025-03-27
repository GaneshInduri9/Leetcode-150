class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        q = deque()
        q.append(root)
        parent = {}

        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    parent[cur.left] = cur
                    q.append(cur.left)

                if cur.right:
                    parent[cur.right] = cur
                    q.append(cur.right)

        q.append((target, 0))
        res = []
        vis = set()
        vis.add(target)
        while q:
            curr, d = q.popleft()
            if d == k:
                res.append(curr.val)
                continue

            if curr.left and curr.left not in vis:
                q.append((curr.left, d + 1))
                vis.add(curr.left)

            if curr.right and curr.right not in vis:
                vis.add(curr.right)
                q.append((curr.right, d + 1))

            if curr in parent and parent[curr] not in vis:
                vis.add(parent[curr])
                q.append((parent[curr], d + 1))

        return res
