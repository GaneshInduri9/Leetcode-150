"""
    There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 
    2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge 
    from node i to each node in graph[i]. A node is a terminal node if there are no outgoing edges. A node is a safe 
    node if every possible path starting from that node leads to a terminal node (or another safe node).
    Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""
from typing import List
class Solution:

    """
        Pre : Cycle detection in directed Graph.
        For a Node to be safe node they dont have to part of cycle and node should not point to a cycle.
        If that's the case then only we can say they are safe nodes.
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        # Intialize
        V = len(graph)
        vis = [0]*V   # visited to make sure we dont revisist them again.
        path = [0]*V  # So if any node is in the same path that means they are leading to a cycle.
        check = [0]*V # check to validate our answers, if this became one that means it lead us to a terminal node and we can say this as a safe node.

        def dfs(node):
            vis[node] = 1
            path[node] = 1
            check[node] = 0

            for neighbour in graph[node]:
                if vis[neighbour] == 0:
                    if dfs(neighbour):
                        # if it leads us to cycle any node in this cycle it will not be an answer.
                        return True
                elif path[neighbour] == 1:
                    # if in the current path than is a cycle so make sure we return true from here.
                    return True
            
            path[node] = 0
            check[node] = 1
            return False

        for i in range(V):
            # Graph might be seperate components.
            if vis[i] == 0:
                dfs(i)
        res = []
        for i in range(V):
            if check[i] == 1:
                # if check eventually became 1 that means this path will eventually leads to answer. 
                res.append(i)
        return res

# Test cases for eventualSafeNodes function
test_cases = [
    # Test Case 1: Simple graph with one terminal node
    ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
    
    # Test Case 2: Fully connected cyclic graph
    ([[1], [2], [0]], []),
    
    # Test Case 3: Graph with multiple disconnected components
    ([[1], [2], [], [4], [5], []], [2, 5]),
    
    # Test Case 4: Directed Acyclic Graph (DAG)
    ([[1, 2], [2, 3], [3], []], [0, 1, 2, 3]),
    
    # Test Case 5: Empty graph
    ([], []),
    
    # Test Case 6: Single terminal node
    ([[]], [0]),
    
    # Test Case 7: Linear chain of nodes
    ([[1], [2], [3], []], [0, 1, 2, 3]),
    
    # Test Case 8: Graph with self-loop
    ([[1], [1]], [])
]

# Running the test cases
solution = Solution()
for i, (graph, expected) in enumerate(test_cases, 1):
    result = solution.eventualSafeNodes(graph)
    print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'} | Output: {result}, Expected: {expected}")




