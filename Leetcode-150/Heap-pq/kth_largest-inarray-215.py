"""
    Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
    By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
    Follow-up: Can you solve it without sorting?    
"""
from typing import List
from heapq import heappop, heappush 
class Solution:

    """ 
        Naive way is to sort and return the k index element but the time is
        O(nlogn). a better way would be to use min_heap while mainatineing 
        the k size.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
            
        return min_heap[0]

# Test cases for the function
def test_findKthLargest():
    solution = Solution()

    # Test Case 1: Basic functionality
    def test_case_1():
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        assert solution.findKthLargest(nums, k) == 5, "Test Case 1 Failed"

    # Test Case 2: All elements are the same
    def test_case_2():
        nums = [1, 1, 1, 1]
        k = 1
        assert solution.findKthLargest(nums, k) == 1, "Test Case 2 Failed"

    # Test Case 3: Single element
    def test_case_3():
        nums = [10]
        k = 1
        assert solution.findKthLargest(nums, k) == 10, "Test Case 3 Failed"

    # Test Case 4: k equals the length of the array
    def test_case_4():
        nums = [7, 6, 5, 4, 3, 2, 1]
        k = 7
        assert solution.findKthLargest(nums, k) == 1, "Test Case 4 Failed"

    # Test Case 5: Negative numbers in the array
    def test_case_5():
        nums = [-1, -2, -3, -4, -5]
        k = 3
        assert solution.findKthLargest(nums, k) == -3, "Test Case 5 Failed"

    # Test Case 6: Mix of positive and negative numbers
    def test_case_6():
        nums = [3, 2, -1, 0, -2, 1]
        k = 4
        assert solution.findKthLargest(nums, k) == 0, "Test Case 6 Failed"

    # Test Case 7: Large k
    def test_case_7():
        nums = [10, 20, 30, 40, 50, 60, 70]
        k = 6
        assert solution.findKthLargest(nums, k) == 20, "Test Case 7 Failed"

    # Run all test cases
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()

    print("All test cases passed!")

# Execute the test function
test_findKthLargest()

        