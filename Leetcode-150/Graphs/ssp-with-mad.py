from typing import List
import heapq


class Solution:
    def MinimumEffort(self, r: int, c: int, heights: List[List[int]]) -> int:
        dist = [[float("inf") for i in range(c)] for j in range(r)]
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0))
        dist[0][0] = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            d, curR, curC = heapq.heappop(min_heap)

            for dr, dc in directions:
                newR, newC = curR + dr, curC + dc
                if newR < r and newR >= 0 and newC < c and newC >= 0:
                    mad = abs(heights[curR][curC] - heights[newR][newC])
                    if max(mad, d) < dist[newR][newC]:
                        dist[newR][newC] = max(mad, d)
                        heapq.heappush(min_heap, (max(mad, d), newR, newC))

        return dist[r - 1][c - 1]


def test_MinimumEffort():
    sol = Solution()

    # Test Case 1: Basic 2x2 grid
    heights = [[1, 2], [3, 4]]
    assert sol.MinimumEffort(2, 2, heights) == 2  # Minimal difference is 1

    # Test Case 2: Single row
    heights = [[1, 3, 6, 10]]
    assert sol.MinimumEffort(1, 4, heights) == 4  # Largest jump is from 1 to 10ß

    print("All test cases passed!")


# Run the test function
test_MinimumEffort()
