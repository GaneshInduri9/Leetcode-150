class Solution:
    """
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    """

    def bellmanFord(self, V, edges, src):
        # code here
        dist = [int(1e8)] * V
        dist[src] = 0
        for i in range(V - 1):
            for sr, dt, w in edges:
                if dist[sr] != int(1e8) and dist[sr] + w < dist[dt]:
                    dist[dt] = dist[sr] + w

        for sr, dt, w in edges:
            if dist[sr] != int(1e8) and dist[sr] + w < dist[dt]:
                return [-1]

        return dist


def test():
    edges = [[0, 1, 5], [1, 0, 3], [1, 2, -1], [2, 0, 1]]
    sol = Solution()
    res = sol.bellmanFord(3, edges, 2)
    print(res)


if __name__ == "__main__":
    test()
