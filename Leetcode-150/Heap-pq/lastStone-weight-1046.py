"""
    You are given an array of integers stones where stones[i] is the weight of the ith stone.
    We are playing a game with the stones. On each turn, we choose the heaviest two stones
    and smash them together. Suppose the heaviest two stones have weights x and y with 
    x <= y. The result of this smash is:
    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x
    At the end of the game, there is at most one stone left.
    Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)

        
        stones.append(0)

        return abs(stones[0])
        
def test_lastStoneWeight():
    sol = Solution()

    # Test case 1: Single stone
    stones = [4]
    assert sol.lastStoneWeight(stones) == 4, f"Test failed for stones: {stones}"

    # Test case 2: Two stones with equal weight
    stones = [5, 5]
    assert sol.lastStoneWeight(stones) == 0, f"Test failed for stones: {stones}"

    # Test case 3: Two stones with different weights
    stones = [10, 4]
    assert sol.lastStoneWeight(stones) == 6, f"Test failed for stones: {stones}"

    # Test case 4: Multiple stones, some of which cancel each other
    stones = [2, 7, 4, 1, 8, 1]
    assert sol.lastStoneWeight(stones) == 1, f"Test failed for stones: {stones}"

    # Test case 5: All stones of the same weight
    stones = [3, 3, 3, 3]
    assert sol.lastStoneWeight(stones) == 0, f"Test failed for stones: {stones}"

    # Test case 6: All stones smash into one last remaining stone
    stones = [1, 3, 2, 7]
    assert sol.lastStoneWeight(stones) == 1, f"Test failed for stones: {stones}"

    # Test case 7: No stones
    stones = []
    assert sol.lastStoneWeight(stones) == 0, f"Test failed for stones: {stones}"

    # Test case 8: Large values
    stones = [20, 10, 15, 8, 25]
    assert sol.lastStoneWeight(stones) == 2, f"Test failed for stones: {stones}"

    print("All test cases passed!")

test_lastStoneWeight()
