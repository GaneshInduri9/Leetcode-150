from typing import List
import heapq


class Solution:
    def findCity(
        self, n: int, m: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:

        adj = [[] for _ in range(n)]

        for sr, dt, w in edges:
            adj[sr].append([dt, w])
            adj[dt].append([sr, w])

        minCity = 1e9
        cityno = 1e9

        for i in range(n):
            min_heap = []
            dist = [float("inf")] * n
            dist[i] = 0
            heapq.heappush(min_heap, (0, i))

            while min_heap:
                currD, currN = heapq.heappop(min_heap)

                for nb, w in adj[currN]:
                    if currD + w < dist[nb]:
                        dist[nb] = currD + w
                        heapq.heappush(min_heap, (currD + w, nb))

            count = 0

            for d in dist:
                if d <= distanceThreshold:
                    count += 1

            if count <= minCity:
                minCity = count
                cityno = i

        return cityno


def test():
    n = 4
    m = 4
    edges = [[0, 1, 3], [1, 2, 1], [2, 3, 1], [3, 0, 1]]
    distanceThreshold = 4
    sol = Solution()
    print(sol.findCity(n, m, edges, distanceThreshold))


if __name__ == "__main__":
    test()
