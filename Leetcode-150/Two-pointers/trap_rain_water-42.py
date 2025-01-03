
"""
    Given n non-negative integers representing an
    elevation map where the width of each bar is 1,
    compute how much water it can trap after raining
    Input: height = [4,2,0,3,2,5]
    Output: 9
    Leetcode - 42
    
    Look at the problem figure to understand better :)
 """

from typing import List
class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # find the left max for each ele
        lmax = 0
        for i in range(n):
            left_max[i] = lmax
            if height[i] > lmax:
                lmax = height[i]
        # find the right max for each ele
        rmax = 0
        for i in range(n-1,-1,-1):
            right_max[i] = rmax
            if height[i] > rmax:
                rmax = height[i]
        
        # once we have found the left and right max then for every element
        # we can find the water storage with min(leftmax,rightMax)-current element
        # height and we can add this to our ans
        ans = 0
        for i in range(n):
            # The water storage will happen only if height[i] < leftmax[i] and rightmax[i]
            if height[i] < left_max[i] and height[i] < right_max[i]:
                 ans += min(left_max[i],right_max[i]) - height[i]
        return ans
    
    """
        Two pointers approach: From the brute force what is causing us the memory
        it's finding the left max and right max right can't we just keep track of
        as we move from both side's if in the we are going to take the min of left and 
        right max only right and which pointer we are going to move is the one which is 
        min of leftmax and rightmax 
    """
    def trap_optimized (self, height: List[int]):
        leftmax, rightmax = 0, 0
        res = 0
        left, right = 1, len(height)-2
        while left <= right:
            leftmax = max(leftmax, height[left-1])
            rightmax = max(rightmax, height[right+1])

            # move the min pointer
            if leftmax <= rightmax:
                if leftmax > height[left]:
                    res += leftmax - height[left]
                left += 1
            else:
                if rightmax > height[right]:
                    res += rightmax- height[right]
                right -= 1
        return res


