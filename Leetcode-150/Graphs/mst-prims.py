from typing import List
import heapq


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    # TC -> O(ELogE) SP -> O(E)
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        min_heap = []
        mst_weight = 0
        vis = [0] * V
        heapq.heappush(min_heap, (0, 0))

        while min_heap:
            w, node = heapq.heappop(min_heap)

            if vis[node] == 0:
                vis[node] = 1
                mst_weight += w

                for dt, w in adj[node]:
                    heapq.heappush(min_heap, (w, dt))

        return mst_weight


def test():
    sol = Solution()

    # Correct adjacency list format
    adj = [
        [(1, 5), (2, 1)],  # Node 0 is connected to 1 (weight 5) and 2 (weight 1)
        [(0, 5), (2, 3)],  # Node 1 is connected to 0 (weight 5) and 2 (weight 3)
        [(0, 1), (1, 3)],  # Node 2 is connected to 0 (weight 1) and 1 (weight 3)
    ]

    res = sol.spanningTree(3, adj)
    print(res)  # Expected output: 4 (Edges: 0-2 (1), 2-1 (3))


if __name__ == "__main__":
    test()
