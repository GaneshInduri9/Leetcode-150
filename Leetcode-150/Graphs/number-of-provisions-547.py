"""
    There are n cities. Some of them are connected, while some are not.
    If city a is connected directly with city b, and city b is connected 
    directly with city c, then city a is connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no
    other cities outside of the group.You are given an n x n matrix isConnected 
    where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
    and isConnected[i][j] = 0 otherwise.
"""
from typing import List
class Solution:
    """
        The question is asking us to find the subgraphs in a graph we can just do 
        a dfs/bfs on every node to see if the node forms a group. if it is a group 
        we know that we visit all the elemnts with dfs/bfs if at node we didn't visit that
        node means this is kind of new group.
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v = len(isConnected)
        adjList = {i: [] for i in range(v)}

        for i in range(v):
            for j in range(v):
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
        
        visit = [0]*(v)
        cnt = 0
        for i in range(v):
            if visit[i] == 0:
                cnt += 1
                self.dfs(i, visit, adjList)
        return cnt
          
    def dfs(self,node, visit, adjList):
        visit[node] = 1
        
        for n in adjList[node]:
            if visit[n] == 0:
                self.dfs(n, visit, adjList)


def test_single_city():
    sol = Solution()
    isConnected = [[1]]
    expected = 1
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_single_city passed!")


def test_two_connected_cities():
    sol = Solution()
    isConnected = [[1, 1], [1, 1]]
    expected = 1
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_two_connected_cities passed!")


def test_two_disconnected_cities():
    sol = Solution()
    isConnected = [[1, 0], [0, 1]]
    expected = 2
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_two_disconnected_cities passed!")


def test_mixed_connections():
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected = 2
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_mixed_connections passed!")


def test_fully_connected():
    sol = Solution()
    isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    expected = 1
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_fully_connected passed!")


def test_multiple_isolated_cities():
    sol = Solution()
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected = 3
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_multiple_isolated_cities passed!")


def test_two_provinces():
    sol = Solution()
    isConnected = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    expected = 2
    result = sol.findCircleNum(isConnected)
    assert result == expected, f"Failed: expected {expected}, got {result}"
    print("test_two_provinces passed!")


# Run all tests
def run_tests():
    test_single_city()
    test_two_connected_cities()
    test_two_disconnected_cities()
    test_mixed_connections()
    test_fully_connected()
    test_multiple_isolated_cities()
    test_two_provinces()
    print("All tests passed!")


# Execute the test suite
run_tests()
