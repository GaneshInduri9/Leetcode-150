class Solution:
    # Function to find if the given edge is a bridge in the graph.
    def isBridge(self, V, adj, c, d):
        time_of_ins = [-1] * V
        min_time = [-1] * V
        vis = [0] * V
        timer = [1]

        def dfs(i, parent):
            vis[i] = 1
            time_of_ins[i] = min_time[i] = timer[0]
            timer[0] += 1

            for nb in adj[i]:
                if nb == parent:
                    continue
                if vis[nb] == 0:
                    if dfs(nb, i):
                        return True
                    if min_time[nb] > time_of_ins[i]:
                        if (i == c and nb == d) or (i == d and nb == c):
                            return True

            for nb in adj[i]:
                if nb != parent:
                    min_time[i] = min(min_time[i], min_time[nb])

            return False

        for i in range(V):
            if vis[i] == 0:
                if dfs(i, -1):
                    return 1
        return 0


# Test Cases
test_cases = [
    # Test Case 1: Simple Bridge
    (3, [[1], [0, 2], [1]], 1, 2, 1),
    # Test Case 2: No Bridge (cycle)
    (4, [[1, 3], [0, 2], [1, 3], [0, 2]], 1, 2, 0),
    # Test Case 3: Disconnected Graph
    (4, [[1], [0], [3], [2]], 2, 3, 1),
    # Test Case 4: Single Edge (Always a Bridge)
    (2, [[1], [0]], 0, 1, 1),
    # Test Case 5: Large Graph with No Bridges
    (5, [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]], 1, 2, 0),
]

sol = Solution()
for V, adj, c, d, expected in test_cases:
    result = sol.isBridge(V, adj, c, d)
    print(f"Edge ({c}, {d}) -> Expected: {expected}, Got: {result}")
