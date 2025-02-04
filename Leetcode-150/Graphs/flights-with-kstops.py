# User function Template for python3
from typing import List
import heapq


class Solution:
    def CheapestFLight(self, n, flights, src, dst, k):
        adj = [[] for i in range(n)]

        for sr, sc, w in flights:
            adj[sr].append([sc, w])

        min_heap = []
        dist = [float("inf")] * n
        # intial configuration
        heapq.heappush(min_heap, (0, src, 0))
        dist[src] = 0

        while min_heap:
            step, curN, d = heapq.heappop(min_heap)

            if step > k:
                continue

            for nb, w in adj[curN]:
                if d + w < dist[nb]:
                    dist[nb] = d + w
                    heapq.heappush(min_heap, (step + 1, nb, d + w))

        if dist[dst] == float("inf"):
            return -1
        return dist[dst]


def test():
    sol = Solution()
    p = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    res = sol.CheapestFLight(4, p, 0, 3, 1)
    print(res)


if __name__ == "__main__":
    test()
