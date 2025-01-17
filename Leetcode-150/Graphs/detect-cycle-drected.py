from typing import List

class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        path = [0] * V  # Tracks nodes in the current recursion stack
        visited = [0] * V  # Tracks if nodes have been fully processed

        def dfs(node):
            visited[node] = 1  # Mark node as visited
            path[node] = 1  # Add node to the recursion stack

            for neighbor in adj[node]:
                if not visited[neighbor]:  # If the neighbor is unvisited
                    if dfs(neighbor):  # Recur for the neighbor
                        return True
                elif path[neighbor]:  # If the neighbor is in the recursion stack
                    return True

            path[node] = 0  # Remove the node from the recursion stack
            return False

        # Check all nodes as the graph may be disconnected
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True

        return False


# Test Cases
def run_tests():
    test_cases = [
        (4, [[1], [2], [3], [1]], True),  # Cycle exists
        (4, [[1], [2], [3], []], False),  # No cycle
        (5, [[1], [2], [0], [4], []], True),  # Cycle in one component
        (6, [[1], [], [3], [], [5], []], False),  # No cycle, disconnected graph
        (1, [[]], False),  # Single node, no edges
        (1, [[0]], True),  # Single node with a self-loop
        (0, [], False),  # Empty graph
        (7, [[1], [2], [0], [4, 5], [5], [6], []], True),  # Larger graph with a cycle
    ]

    print("Running Test Cases:")
    for i, (V, adj, expected) in enumerate(test_cases, 1):
        solution = Solution()
        result = solution.isCyclic(V, adj)
        print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'}")

# Main Script
if __name__ == "__main__":
    run_tests()
