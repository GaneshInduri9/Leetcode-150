from typing import List
from collections import defaultdict
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for sr, dt, w in roads:
            adj[sr].append([dt, w])
            adj[dt].append([sr, w])

        min_heap = []
        dist = [float("inf")] * (n)
        dist[0] = 0
        ways = [0] * (n)
        ways[0] = 1
        heapq.heappush(min_heap, (0, 0))
        mod = (10**9) + 7

        while min_heap:
            d, curN = heapq.heappop(min_heap)

            for nb, w in adj[curN]:
                if d + w < dist[nb]:
                    heapq.heappush(min_heap, (d + w, nb))
                    dist[nb] = d + w
                    ways[nb] = ways[curN]
                elif d + w == dist[nb]:
                    ways[nb] = (ways[nb] + ways[curN]) % mod
        return ways[n - 1] % mod


def test():
    n = 7
    roads = [
        [0, 6, 7],
        [0, 1, 2],
        [1, 2, 3],
        [1, 3, 3],
        [6, 3, 3],
        [3, 5, 1],
        [6, 5, 1],
        [2, 5, 1],
        [0, 4, 5],
        [4, 6, 2],
    ]
    sol = Solution()
    res = sol.countPaths(n, roads)
    print(res)


if __name__ == "__main__":
    test()
