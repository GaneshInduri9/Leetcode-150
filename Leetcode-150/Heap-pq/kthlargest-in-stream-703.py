"""
    You are part of a university admissions office and need to keep track of the kth highest 
    test score from applicants in real-time. This helps to determine cut-off marks for interviews
    and admissions dynamically as new applicants submit their scores.
    You are tasked to implement a class which, for a given integer k, maintains a stream of test 
    scores and continuously returns the kth highest test score after a new score has been submitted.
    More specifically, we are looking for the kth highest score in the sorted list of all scores
"""
from typing import List
from heapq import heapify, heappop, heappush
class KthLargest:

    """
        The brute force way would be to add all the elements to heap
        and then return the k the element from the last but that just takes 
        more time and space we would end up storing all the elements in the heap.
        But why do we need the smaller elements than k actuallly can't we just kick out
        the elements that we don't need in this case why do we need the smaller elemnts 
        than k. So what if we maintain a heap with k size in that way when ever an element 
        needs to be added to the steram we can add it heap and than kick out the 
        min element right since we want to mainatain only the k large elements.
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapify(self.minHeap)
        while len(self.minHeap)> k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]

def test_kth_largest():
    # Test Case 1: Basic functionality with initial elements
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(3) == 4, "Test Case 1 Failed"
    assert kthLargest.add(5) == 5, "Test Case 1 Failed"
    assert kthLargest.add(10) == 5, "Test Case 1 Failed"
    assert kthLargest.add(9) == 8, "Test Case 1 Failed"
    assert kthLargest.add(4) == 8, "Test Case 1 Failed"

    # Test Case 2: Empty initial list
    k = 1
    nums = []
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-1) == -1, "Test Case 2 Failed"
    assert kthLargest.add(1) == 1, "Test Case 2 Failed"
    assert kthLargest.add(-2) == 1, "Test Case 2 Failed"
    assert kthLargest.add(3) == 3, "Test Case 2 Failed"
    
    # Test Case 3: Single element in the initial list
    k = 1
    nums = [5]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(6) == 6, "Test Case 3 Failed"
    assert kthLargest.add(4) == 6, "Test Case 3 Failed"

    # Test Case 4: k larger than the initial list size
    k = 4
    nums = [2, 3]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(1) == 1, "Test Case 4 Failed"
    assert kthLargest.add(4) == 1, "Test Case 4 Failed"
    assert kthLargest.add(5) == 2, "Test Case 4 Failed"

    # Test Case 5: Negative numbers in the input
    k = 2
    nums = [-10, -20, -30]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-15) == -15, "Test Case 5 Failed"
    assert kthLargest.add(-5) == -10, "Test Case 5 Failed"

    print("All test cases passed!")

# Run the tests
test_kth_largest()
