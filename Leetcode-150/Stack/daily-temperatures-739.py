"""
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have 
    to wait after the ith day to get a warmer temperature. If there is no future 
    day for which this is possible, keep answer[i] == 0 instead.

    Input: temperatures = [30,38,30,36,35,40,28]
    Output: [1,4,1,2,1,0,0]

"""
from typing import List
class Solution:
    """
        Brute Force would be to start iterating from start and find the next greater element in
        the array after this so this would be O(n^2).
        The optimized way is think as we move forward what if we can remember the elements that 
        occured when we find a greater element than this we can update this result we can do this 
        with monotonically decreasing stack so when ever we element greater than our top of stack 
        we pop the elements in the stack to find a smaller elemts and we do this while updating the 
        results.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        stack.append([temperatures[0], 0])
        res = [0]*n
        for i in range(1,n):
            while stack and temperatures[i] > stack[-1][0]:
                ele, index = stack.pop()
                res[index] = i - index
            stack.append([temperatures[i], i])
        return res

if __name__ == "__main__":
    # Create an object of the Solution class
    solution = Solution()
    
    # Define the input
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    
    # Call the dailyTemperatures method
    result = solution.dailyTemperatures(temperatures)
    
    # Print the result
    print("Input Temperatures:", temperatures)
    print("Days to Wait for Warmer Temperature:", result)