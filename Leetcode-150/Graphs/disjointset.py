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


def test():
    d = DisjointSet(7)
    d.unionByRank(1, 2)
    d.unionByRank(2, 3)
    d.unionByRank(4, 5)
    d.unionByRank(6, 7)
    d.unionByRank(5, 6)

    if d.findParent(3) == d.findParent(7):
        print("same brfore union")
    else:
        print("not same before union")

    d.unionByRank(3, 7)

    if d.findParent(3) == d.findParent(7):
        print("same after union")
    else:
        print("not same after union")


if __name__ == "__main__":
    test()
