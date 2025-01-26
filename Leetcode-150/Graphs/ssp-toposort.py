#User function Template for python3
from typing import List
from collections import deque

class Solution:
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        dist = [float('inf')] * V  # Initialize distances as infinity
        inDegree = [0] * V
        adj = [[] for _ in range(V)]

        # Build adjacency list and calculate in-degrees
        for node, nb, w in edges:
            adj[node].append((nb, w))
            inDegree[nb] += 1

        # Initialize queue with all nodes having in-degree of 0
        q = deque()
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)

        dist[0] = 0  # Distance to the source is always 0
        topo = []

        # Perform topological sort
        while q:
            node = q.popleft()
            topo.append(node)
            for nb, w in adj[node]:
                inDegree[nb] -= 1
                if inDegree[nb] == 0:
                    q.append(nb)

        # Relax edges in topological order
        for node in topo:
            if dist[node] != float('inf'):  # Only process reachable nodes
                for nb, w in adj[node]:
                    if dist[node] + w < dist[nb]:
                        dist[nb] = dist[node] + w

        # Replace infinity distances with -1
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist


def test():
    sol = Solution()
    V = 6
    E = 7
    edges = [
        [0, 1, 2],
        [0, 4, 1],
        [1, 2, 3],
        [4, 2, 2],
        [4, 5, 4],
        [2, 3, 6],
        [5, 3, 1]
    ]
    print(sol.shortestPath(V, E, edges))

if __name__ == "__main__":
    test()
                

                



