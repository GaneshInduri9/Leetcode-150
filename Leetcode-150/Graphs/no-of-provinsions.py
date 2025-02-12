class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ul_pu = self.findUParent(u)
        ul_pv = self.findUParent(v)

        if self.rank[ul_pv] < self.rank[ul_pu]:
            self.parent[ul_pv] = ul_pu

        elif self.rank[ul_pu] < self.rank[ul_pv]:
            self.parent[ul_pu] = ul_pv

        else:
            self.parent[ul_pu] = ul_pv
            self.rank[ul_pv] += 1


class Solution:
    def numProvinces(self, adj, V):
        D = DisJointSet(V)

        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    D.union(i, j)
        cnt = 0
        for i in range(V):
            if D.parent[i] == i:
                cnt += 1
        return cnt


def test():
    s = Solution()
    adj = [[1, 1], [1, 1]]
    sol = s.numProvinces(adj, 2)
    print(sol)


if __name__ == "__main__":
    test()
