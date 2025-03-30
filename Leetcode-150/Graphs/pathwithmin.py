class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        min_heap = []
        dist = [[float("inf") for i in range(m)] for _ in range(n)]

        heapq.heappush(min_heap, (0, 0, 0))
        dist[0][0] = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                newr = dr + r
                newc = dc + c
                if newr < n and newr >= 0 and newc < m and newc >= 0:
                    newEffort = max(effort, abs(heights[newr][newc] - heights[r][c]))
                    if newEffort < dist[newr][newc]:
                        dist[newr][newc] = newEffort
                        heapq.heappush(min_heap, (newEffort, newr, newc))

        return dist[n - 1][m - 1]
