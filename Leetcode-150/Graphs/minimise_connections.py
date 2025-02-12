"""
    Given an integer N, denoting the number of computers connected by 
    cables forming a network and a 2d array connections[][], with each 
    row (i, j) representing a connection between ith and jth computer, 
    the task is to connect all the computers either directly or indirectly by 
    removing any of the given connections and connecting two disconnected computers. 
    If its not possible to connect all the computers, return -1. 
    Otherwise, return the minimum number of such operations required.
"""

from typing import List


class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.emptyEdges = 0

    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ul_pu = self.findUParent(u)
        ul_pv = self.findUParent(v)

        if ul_pu == ul_pv:
            self.emptyEdges += 1
            return

        if self.rank[ul_pv] < self.rank[ul_pu]:
            self.parent[ul_pv] = ul_pu

        elif self.rank[ul_pu] < self.rank[ul_pv]:
            self.parent[ul_pu] = ul_pv

        else:
            self.parent[ul_pu] = ul_pv
            self.rank[ul_pv] += 1


class Solution:
    def minimumConnections(self, n: int, connections: List[List[int]]) -> int:
        D = DisJointSet(n)

        for u, v in connections:
            D.union(u, v)

        numComponents = sum(1 for i in range(n) if D.findUParent(i) == i)

        if D.emptyEdges < numComponents - 1:
            return -1

        return numComponents - 1


def test():
    s = Solution()
    res = s.minimumConnections(4, [[0, 1], [0, 2], [1, 2]])
    print(res)


if __name__ == "__main__":
    test()
