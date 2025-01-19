"""
    Topological sort says that if there is an edge between u and v then u should come before V.
    This should be true for every component in the graph.

    We will use recursion + stack we call a dfs for unvisited node then we try to visit it's neighbours
    and when coming back we push this node to stack. Well this works but how simple if we are pushing them 
    to stack the most recent completed node will be present on top of stack and the least recent will 
    be at the bottom of the stack. 
"""
class Solution:
    # Function to return list containing vertices in Topological order.
    def topologicalSort(self, adj):
        V = len(adj)
        vis = [0] * V
        stack = []

        def dfs(node):
            vis[node] = 1
            for neighbour in adj[node]:
                if vis[neighbour] == 0:
                    dfs(neighbour)
            stack.append(node)

        for i in range(V):
            if vis[i] == 0:
                dfs(i)

        return stack[::-1]


def test_topological_sort():
    solution = Solution()
    
    test_cases = [
        {
            "adj": [[1, 2], [2], []],
            "expected": [0, 1, 2],
            "description": "Graph with 3 nodes and dependencies",
        },
        {
            "adj": [[1], [2], [3], []],
            "expected": [0, 1, 2, 3],
            "description": "Linear graph with 4 nodes",
        },
        {
            "adj": [[1, 2], [3], [3], []],
            "expected": [0, 2, 1, 3],
            "description": "Graph with a common dependency",
        },
        {
            "adj": [[], [0], [0], [1, 2]],
            "expected": [3, 2, 1, 0],
            "description": "Graph with multiple roots pointing to a single node",
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        adj = test["adj"]
        expected = test["expected"]
        description = test["description"]

        print(f"Test Case {i}: {description}")
        print(f"Adjacency List: {adj}")
        
        result = solution.topologicalSort(adj)
        
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test failed for {description}"
        print(f"Test Case {i} passed!\n")

# Run the test function
test_topological_sort()
