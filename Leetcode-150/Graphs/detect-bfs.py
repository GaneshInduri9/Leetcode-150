from typing import List
from collections import deque

class Solution:
    """
		If the graph doesn't have any cycle we wouln't comeback to same node if a different parent here
		draw cyclic grapfh to understand why this works. When evr we are checking neighbours for any node if this
		has a neighbour for which this is not a parent that means that node is connected to somether parent node
		this indiactes that if we go to this node then it means we are visiting it from a different parent and this
		causes a cycle.
	"""
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V  # Track visited nodes
        q = deque()  # Queue for BFS

        def detect(sr: int) -> bool:
            q.append((sr, -1))  # Append starting node and parent (-1 for no parent)
            visited[sr] = 1

            while q:
                node, parent = q.popleft()
                for neighbor in adj[node]:
                    if visited[neighbor] == 0:  # If neighbor is not visited
                        visited[neighbor] = 1
                        q.append((neighbor, node))
                    elif neighbor != parent:  # If neighbor is visited and not parent
                        return True
            return False

        # Check all components of the graph
        for i in range(V):
            if visited[i] == 0:  # If the node is unvisited
                if detect(i):  # Perform BFS from the node
                    return True
        return False
    
    def isCycleDfs(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V  # Track visited nodes

        def detect(node, parent) -> bool:
            visited[node] = 1
            for neighbour in adj[node]:
                if visited[neighbour] == 0:
                    if detect(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
                
            return False

        # Check all components of the graph
        for i in range(V):
            if visited[i] == 0:  # If the node is unvisited
                if detect(i,-1):  # Perform BFS from the node
                    return True
        return False
    
# Helper function to create an adjacency list
def create_adj_list(edges, V):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

# Test case 1: Graph with a cycle
edges = [[0, 1], [1, 2], [2, 0]]
V = 3
adj = create_adj_list(edges, V)
solution = Solution()
assert solution.isCycle(V, adj) == True, "Test case 1 failed."
assert solution.isCycleDfs(V, adj) == True, "Test case 1 failed."

# Test case 2: Graph without a cycle
edges = [[0, 1], [1, 2]]
V = 3
adj = create_adj_list(edges, V)
assert solution.isCycle(V, adj) == False, "Test case 2 failed."
assert solution.isCycleDfs(V, adj) == False, "Test case 2 failed."

# Test case 3: Disconnected graph with a cycle
edges = [[0, 1], [1, 2], [2, 0], [3, 4]]
V = 5
adj = create_adj_list(edges, V)
assert solution.isCycle(V, adj) == True, "Test case 3 failed."
assert solution.isCycleDfs(V, adj) == True, "Test case 3 failed."

# Test case 4: Empty graph (no edges)
edges = []
V = 3
adj = create_adj_list(edges, V)
assert solution.isCycle(V, adj) == False, "Test case 4 failed."
assert solution.isCycleDfs(V, adj) == False, "Test case 4 failed."

# Test case 5: Single node graph (no edges)
edges = []
V = 1
adj = create_adj_list(edges, V)
assert solution.isCycle(V, adj) == False, "Test case 5 failed."
assert solution.isCycleDfs(V, adj) == False, "Test case 5 failed."

print("All test cases passed!")
