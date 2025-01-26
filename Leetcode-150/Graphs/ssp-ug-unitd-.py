from collections import deque


class Solution:
    def shortestPath(self, adj, src):
        V = len(adj)
        dist = [float("inf")] * V

        q = deque()
        q.append(src)
        dist[src] = 0

        while q:
            node = q.popleft()
            for nb in adj[node]:
                if dist[node] + 1 < dist[nb]:
                    dist[nb] = dist[node] + 1
                    q.append(nb)

        for i in range(V):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


def test():
    sol = Solution()
    V = 6
    E = 7
    edges = [
        [0, 1],
        [0, 4],
        [1, 2],
        [4, 2],
        [4, 5],
        [2, 3],
        [5, 3],
    ]
    adj = [[] for _ in range(V)]
    for node, nb in edges:
        adj[node].append(nb)
        adj[nb].append(node)  # Assuming undirected graph

    src = 0
    print(sol.shortestPath(adj, src))


if __name__ == "__main__":
    test()
