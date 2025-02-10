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


def test():
    d = DisjointSet(7)
    d.union(1, 2)
    d.union(2, 3)
    d.union(4, 5)
    d.union(6, 7)
    d.union(5, 6)

    if d.findParent(3) == d.findParent(7):
        print("same brfore union")
    else:
        print("not same before union")

    d.union(3, 7)

    if d.findParent(3) == d.findParent(7):
        print("same after union")
    else:
        print("not same after union")


if __name__ == "__main__":
    test()
