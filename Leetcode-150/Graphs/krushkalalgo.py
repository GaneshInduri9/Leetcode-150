from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
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


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        edges = []
        d = DisjointSet(V)

        for u in range(V):
            for v, w in adj[u]:  # Each adj[u] contains (neighbor, weight)
                if u < v:  # Avoid adding the same edge twice
                    edges.append((w, u, v))
        mst = 0
        edges.sort()
        E = len(edges)
        for i in range(E):
            w, u, v = edges[i]
            if d.findParent(u) != d.findParent(v):
                mst += w
                d.union(u, v)

        return mst


def test():
    V = 4
    adj = [
        [[1, 1], [2, 2]],  # Node 0 → (1,1), (2,2)
        [[0, 1], [2, 3], [3, 4]],  # Node 1 → (0,1), (2,3), (3,4)
        [[0, 2], [1, 3], [3, 5]],  # Node 2 → (0,2), (1,3), (3,5)
        [[1, 4], [2, 5]],  # Node 3 → (1,4), (2,5)
    ]

    sol = Solution()
    res = sol.spanningTree(V, adj)
    print(res)


if __name__ == "__main__":
    test()
