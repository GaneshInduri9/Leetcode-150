"""
    You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
    Each CPU interval can be idle or allow the completion of one task. Tasks can be completed 
    in any order, but there's a constraint: there has to be a gap of at least n intervals 
    between two tasks with the same label.Return the minimum number of CPU intervals required 
    to complete all tasks.
"""
from collections import Counter, deque
import heapq
from typing import List
class Solution:

    """
        The idea is to complete the task that has higher  frequency, the intuation behind this
        If we try to solve lower-frequency tasks first, we may end up with idle slots later 
        because higher-frequency tasks might not have enough "space" to fit without violating
        the cooldown rule. The queue is to keep track when this task again will be available for as
        we process more tasks.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]

        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while q or max_heap:
            time += 1
            if max_heap:
                cnt = 1+ heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
def test_least_interval():
    solution = Solution()
    
    # Test Case 1: All tasks different, no cooldown
    assert solution.leastInterval(["A", "B", "C", "D"], 0) == 4, "Test Case 1 Failed"

    # Test Case 2: Single task repeated with no cooldown
    assert solution.leastInterval(["A", "A", "A", "A"], 0) == 4, "Test Case 2 Failed"

    # Test Case 3: Tasks repeated with cooldown
    assert solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8, "Test Case 3 Failed"

    # Test Case 4: Tasks with cooldown requiring idle times
    assert solution.leastInterval(["A", "A", "A", "B", "B", "C"], 2) == 7, "Test Case 4 Failed"

    # Test Case 5: Single task repeated with large cooldown
    assert solution.leastInterval(["A", "A", "A", "A"], 3) == 13, "Test Case 5 Failed"

    # Test Case 6: No tasks
    assert solution.leastInterval([], 2) == 0, "Test Case 6 Failed"

    # Test Case 7: Multiple tasks with no cooldown
    assert solution.leastInterval(["A", "A", "B", "B"], 0) == 4, "Test Case 7 Failed"

    # Test Case 8: Edge case with only one task
    assert solution.leastInterval(["A"], 2) == 1, "Test Case 8 Failed"

    print("All test cases passed!")

# Run the tests
test_least_interval()
