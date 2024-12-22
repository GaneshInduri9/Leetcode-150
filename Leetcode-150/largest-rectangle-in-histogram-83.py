"""
    Given an array of integers heights representing the histogram's bar height where the 
    width of each bar is 1, return the area of the largest rectangle in the histogram.

    ex: heights = [2,1,5,6,2,3]
    op: 10
    "Draw a histogram graph representaion of this to understand the problem statement better :)"
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculate the largest rectangle area in the histogram.
        Uses a monotonic stack to efficiently find the largest area.
        """
        stack = []  # Stack to store indices of histogram bars
        maxArea = 0  # Variable to track the maximum area
        n = len(heights)

        for i in range(n):
            # Process bars that are taller than the current bar
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()  # Index of the bar to process
                height = heights[index]  # Height of the rectangle
                # Calculate width using previous smaller element (PSE) and next smaller element (NSE)
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)  # Push the current index to the stack

        # Process remaining bars in the stack
        while stack:
            index = stack.pop()
            height = heights[index]
            width = n if not stack else n - stack[-1] - 1
            maxArea = max(maxArea, height * width)

        return maxArea


# Test cases to validate the solution
def testLargestRectangleArea():
    solution = Solution()

    examples = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([6, 2, 5, 4, 5, 1, 6], 12),
        ([1, 1, 1, 1, 1], 5),
        ([0], 0),
        ([1, 2, 3, 4, 5], 9),
    ]

    for heights, expected in examples:
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights} | Expected: {expected} | Result: {result}")


# Run the tests
if __name__ == "__main__":
    testLargestRectangleArea()




        
                

        

             
