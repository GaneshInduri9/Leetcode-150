"""
    So kahn's is way to solve topological sort. So what does topological sort state: if there is an edge between u and v 
    u always appears before v and this will be recursively true for every connected node.

    So now we know that khan's algo uses bfs so we definatly need a queue and we need a indegree array keeping tab of 
    what's the indegree of each node in the graph.
"""
from collections import deque

class Solution:
    def kahnsAlgoBfs(self, adj):
        V = len(adj)  # Number of vertices
        indegree = [0] * V

        # Calculate indegree for each node
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1

        # Initialize the queue with nodes having indegree 0
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        res = []
        count = 0  # To track processed nodes

        # Process nodes using BFS
        while q:
            node = q.popleft()
            res.append(node)

            # Reduce the indegree of neighbors
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Check for cycles
        if len(res) != V:
            return "Cycle detected, no valid topological order"
        
        return res

# Test the implementation
def test_kahn_algo():
    sol = Solution()

    # Example graph
    adj = [[], [], [3], [1], [1, 0], [0, 2]]
    print("Topological Sort:", sol.kahnsAlgoBfs(adj))

    # Graph with a cycle
    adj_with_cycle = [[1], [2], [0], [4], []]
    print("Topological Sort with Cycle:", sol.kahnsAlgoBfs(adj_with_cycle))

    # Empty graph
    empty_adj = []
    print("Empty Graph:", sol.kahnsAlgoBfs(empty_adj))

if __name__ == "__main__":
    test_kahn_algo()
