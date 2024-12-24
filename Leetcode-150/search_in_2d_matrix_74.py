from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        end = rows * cols
        beg = 0
        while beg < end:
            mid = beg + (end - beg) // 2
            # why doing devision on at that index gives us
            # row if u see each will start at the multiple of 
            # our col lenght and if we want to get which row is it 
            # part we can do // by col lenght and module gives us the 
            # reminder the col lenght ex in 3X4 matrix 
            # if the mid is 5 if we wanted to get the row if we do // we get the row
            # % gives us the col 
            # pretty cool is in't it ? 
            ele = matrix[mid // cols][mid % cols]
            if ele == target:
                return True
            if target > ele:
                beg = mid + 1
            else:
                end = mid
        return False

def main():
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
        ([[1, 2, 3, 4, 5]], 4, True),
        ([[1, 2, 3, 4, 5]], 6, False),
        ([[1, 3], [5, 7]], 5, True),
        ([[1, 3], [5, 7]], 2, False),
    ]

    # Run test cases
    for i, (matrix, target, expected) in enumerate(test_cases):
        result = solution.searchMatrix(matrix, target)
        assert result == expected, f"Test case {i + 1} failed: Expected {expected}, Got {result}"
        print(f"Test case {i + 1} passed.")

if __name__ == "__main__":
    main()
