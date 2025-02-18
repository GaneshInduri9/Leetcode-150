class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ul_pu = self.findParent(u)
        ul_pv = self.findParent(v)

        if ul_pu == ul_pv:
            return

        ru = self.rank[ul_pu]
        rv = self.rank[ul_pv]

        if rv < ru:
            self.parent[ul_pv] = ul_pu
        elif ru < rv:
            self.parent[ul_pu] = ul_pv
        else:
            self.parent[ul_pv] = ul_pu
            self.rank[ul_pu] += 1

    def unionBySize(self, u, v):
        ul_pu = self.findParent(u)
        ul_pv = self.findParent(v)

        if ul_pu == ul_pv:
            return

        if self.size[ul_pu] < self.size[ul_pv]:
            self.parent[ul_pu] = ul_pv
            self.size[ul_pv] += self.size[ul_pu]
        else:
            self.parent[ul_pv] = ul_pu
            self.size[ul_pu] += self.size[ul_pv]


from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        max_row = 0
        max_col = 0
        n = len(stones)

        for r, c in stones:
            max_row = max(r, max_row)
            max_col = max(max_col, c)

        D = DisjointSet(max_col + max_row + 1)

        stoneNode = defaultdict(int)
        for i in range(n):
            nodeRow = stones[i][0]
            nodeCol = stones[i][1] + max_row + 1
            D.unionBySize(nodeRow, nodeCol)
            stoneNode[nodeRow] = 1
            stoneNode[nodeCol] = 1
        ans = 0
        for key, value in stoneNode.items():
            if D.findParent(key) == key:
                ans += 1
        return n - ans
