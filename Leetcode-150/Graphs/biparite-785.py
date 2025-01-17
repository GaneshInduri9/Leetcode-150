from typing import List
from collections import deque
class Solution:

    """
        A Bipartite is something if we try to color the graph with any two colors such that no adjancet 
        nodes have the same color the idea is brute force way of doing this we start from any node and
        do a travesal while making sure that if the neighbour is visted it is of different color.
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        def check(start):
            q = deque()
            color[start] = 0
            q.append(start)

            while q:
                node = q.pop()

                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        q.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False
                
            return True
        
        for i in range(n):
            if color[i] == -1:
                if check(i) == False:
                    return False
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Simple bipartite graph
    graph1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(solution.isBipartite(graph1))  # Expected: True

    # Test case 2: Not a bipartite graph (odd cycle)
    graph2 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(solution.isBipartite(graph2))  # Expected: False

    # Test case 3: Disconnected graph, each component is bipartite
    graph3 = [[1], [0], [3], [2]]
    print(solution.isBipartite(graph3))  # Expected: True

    # Test case 4: Single node graph (trivial bipartite)
    graph4 = [[]]
    print(solution.isBipartite(graph4))  # Expected: True

    # Test case 5: Empty graph
    graph5 = []
    print(solution.isBipartite(graph5))  # Expected: True

    # Test case 6: Larger bipartite graph
    graph6 = [[1, 2], [0, 3], [0, 3], [1, 2]]
    print(solution.isBipartite(graph6))  # Expected: True
