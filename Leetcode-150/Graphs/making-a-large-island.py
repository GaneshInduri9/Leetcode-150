from typing import List


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


class Solution:
    def isValid(self, r, c, n):
        return 0 <= r < n and 0 <= c < n

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        D = DisjointSet(n * n)
        max_size = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                node = (row * n) + col
                for dr, dc in directions:
                    newR = dr + row
                    newC = dc + col
                    if self.isValid(newR, newC, n):
                        if grid[newR][newC] == 1:
                            adjN = (newR * n) + newC
                            D.unionBySize(adjN, node)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue

                comp = set()
                for dr, dc in directions:
                    newR, newC = dr + row, dc + col
                    if self.isValid(newR, newC, n):
                        if grid[newR][newC] == 1:
                            adjN = (newR * n) + newC
                            comp.add(adjN)
                size = 0
                for node in comp:
                    size += D.size[node]

                max_size = max(size + 1, max_size)

        for cell in range((n * n)):
            max_size = max(max_size, D.size[D.findParent(cell)])
        return max_size
