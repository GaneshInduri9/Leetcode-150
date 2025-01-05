"""
    Given an array of points where points[i] = [xi, yi] represents a point 
    on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance (
    i.e., √(x1 - x2)2 + (y1 - y2)2).You may return the answer in any order. 
    The answer is guaranteed to be unique (except for the order that it is in).
"""

from heapq import heappop, heappush 
from typing import List
class Solution:

    """
        The brute force way would be to find the distance of each point and store them in some data 
        structure so that we can sort them and return the k closest elements to origin.
        A better way would be to use a heap, the intualtion behind putting - negative values 
        is so that when ever we see a smaller element we would want to pop the larger element first
        when the size exceeds more than k (the larger elements comes in front) 
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        n = len(points)

        for i in range(n):
            x, y = points[i]

            dist = x*x + y*y
            heappush(min_heap, (-dist, [x,y]))

            if len(min_heap) > k:
                heappop(min_heap)
        
        res = []
        for dist, point in min_heap:
            res.append(point)
        
        return res

# Test cases
solution = Solution()

# Test case 1: Simple case with k=1
points = [[1, 3], [-2, 2]]
k = 1
print(solution.kClosest(points, k))  # Expected output: [[-2, 2]]

# Test case 2: More points, k=2
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(solution.kClosest(points, k))  # Expected output: [[3, 3], [-2, 4]] or any order of the two closest points

# Test case 3: All points are returned
points = [[1, 1], [2, 2], [3, 3]]
k = 3
print(solution.kClosest(points, k))  # Expected output: [[1, 1], [2, 2], [3, 3]]

# Test case 4: Handling a mix of positive and negative coordinates
points = [[-2, -4], [0, 0], [2, 2], [-1, 1], [3, -3]]
k = 2
print(solution.kClosest(points, k))  # Expected output: [[0, 0], [-1, 1]] or another valid pair of closest points

# Test case 5: Single point with k=1
points = [[1, 1]]
k = 1
print(solution.kClosest(points, k))  # Expected output: [[1, 1]]

# Test case 6: Points with equal distances
points = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
k = 2
print(solution.kClosest(points, k))  # Expected output: Any two points with the same distance, e.g., [[1, 1], [-1, -1]]

# Test case 7: Larger number of points
points = [[i, i + 1] for i in range(100)]  # Points like [0, 1], [1, 2], ..., [99, 100]
k = 5
print(solution.kClosest(points, k))  # Expected output: The 5 points closest to origin, e.g., [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]

# Test case 8: k larger than the number of points
points = [[1, 2], [3, 4]]
k = 5
print(solution.kClosest(points, k))  # Expected output: [[1, 2], [3, 4]]

# Test case 9: k = 0 (edge case)
points = [[1, 2], [3, 4]]
k = 0
print(solution.kClosest(points, k))