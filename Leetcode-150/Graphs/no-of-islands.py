"""
    You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
Note : An island means group of 1s such that they share a common side.
"""


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


from typing import List


class Solution:

    def isValid(self, rows, cols, r, c):
        if r >= 0 and r < rows and c >= 0 and c < cols:
            return True
        return False

    def numOfIslands(
        self, rows: int, cols: int, operators: List[List[int]]
    ) -> List[int]:
        """Find No of Islands

        Args:
            rows (int):
            cols (int):
            operators (List[List[int]]): connections

        Returns:
            List[int]: no of connected componets at each operator
        """

        n = len(operators)
        res = []
        D = DisjointSet((rows * cols))
        vis = [[0 for i in range(cols)] for j in range(rows)]
        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r, c in operators:
            if vis[r][c] == 1:
                res.append(count)
                continue

            vis[r][c] = 1
            count += 1

            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if self.isValid(rows, cols, newR, newC):
                    if vis[newR][newC] == 1:
                        node = (r * cols) + c
                        adjN = (newR * cols) + newC
                        if D.findParent(node) != D.findParent(adjN):
                            count -= 1
                            D.union(node, adjN)

            res.append(count)

        return res


def test():
    s = Solution()
    operators = [[1, 1], [0, 1], [3, 3], [3, 4]]
    res = s.numOfIslands(4, 5, operators)
    print(res)


if __name__ == "__main__":
    test()
