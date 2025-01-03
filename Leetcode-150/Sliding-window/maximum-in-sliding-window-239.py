"""
    You are given an array of integers nums, there is a sliding window of size
    k which is moving from the very left of the array to the very right. You can
    only see the k numbers in the window. Each time the sliding window moves right 
    by one position. Return the max sliding window.
"""
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        if n <= k:
            return [max(nums)]
        for i in range(n-k+1):
            currMax = nums[i]
            for j in range(i+1,i+k):
                if nums[j]>currMax:
                    currMax = nums[j]
            res.append(currMax)
        return res
    
    """ def maxSlidingWindowOptimal(self, nums: List[int], k: int) -> List[int]: """
           
