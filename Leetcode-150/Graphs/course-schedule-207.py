from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n)]
        for pre in prerequisites:
            v, u = pre
            adj[u].append(v)
        
        indgree = [0]*n
        for i in range(n):
            for ne in adj[i]:
                indgree[ne] += 1
        
        q = deque()
        for i in range(n):
            if indgree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for ne in adj[node]:
                indgree[ne] -= 1
                if indgree[ne] == 0:
                    q.append(ne)
                
        if len(res) == n:
            return True
        return False

def test_canFinish():
    sol = Solution()

    # Test Case 1: No prerequisites (All courses can be finished)
    numCourses = 4
    prerequisites = []
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 1 Failed"

    # Test Case 2: Simple case with no cycle
    numCourses = 2
    prerequisites = [[1, 0]]
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 2 Failed"

    # Test Case 3: Simple case with a cycle
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert sol.canFinish(numCourses, prerequisites) == False, "Test Case 3 Failed"

    # Test Case 4: Multiple courses with no cycle
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 4 Failed"

    # Test Case 5: Multiple courses with a cycle
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]
    assert sol.canFinish(numCourses, prerequisites) == False, "Test Case 5 Failed"

    # Test Case 6: Disconnected graph (No cycle)
    numCourses = 6
    prerequisites = [[1, 0], [4, 3]]
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 6 Failed"

    # Test Case 7: Single course with no prerequisites
    numCourses = 1
    prerequisites = []
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 7 Failed"

    # Test Case 8: Single course with self-loop (cycle)
    numCourses = 1
    prerequisites = [[0, 0]]
    assert sol.canFinish(numCourses, prerequisites) == False, "Test Case 8 Failed"

    # Test Case 9: Larger graph with multiple components and no cycles
    numCourses = 6
    prerequisites = [[1, 0], [2, 1], [4, 3], [5, 4]]
    assert sol.canFinish(numCourses, prerequisites) == True, "Test Case 9 Failed"

    # Test Case 10: Larger graph with multiple components and a cycle
    numCourses = 6
    prerequisites = [[1, 0], [2, 1], [4, 3], [5, 4], [3, 5]]
    assert sol.canFinish(numCourses, prerequisites) == False, "Test Case 10 Failed"

    print("All test cases passed!")

# Run the test function
test_canFinish()
