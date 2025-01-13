from typing import List
class Solution:
    "If you read the problem carefully it is asking us to explore us given source explore all the neighbours"
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        sourcepixl = image[sr][sc]

        if sourcepixl == color:
            return image
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != sourcepixl:
                return 
            
            image[r][c] = color

            # dfs on neighbours
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image

    def test(self):
        # Test case 1
        image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr1, sc1, color1 = 1, 1, 2
        result1 = self.floodFill(image1, sr1, sc1, color1)
        expected1 = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        print("Test 1 Passed" if result1 == expected1 else f"Test 1 Failed: {result1}")

        # Test case 2
        image2 = [[0, 0, 0], [0, 0, 0]]
        sr2, sc2, color2 = 0, 0, 2
        result2 = self.floodFill(image2, sr2, sc2, color2)
        expected2 = [[2, 2, 2], [2, 2, 2]]
        print("Test 2 Passed" if result2 == expected2 else f"Test 2 Failed: {result2}")

        # Test case 3
        image3 = [[0, 0, 0], [0, 1, 1]]
        sr3, sc3, color3 = 1, 1, 1
        result3 = self.floodFill(image3, sr3, sc3, color3)
        expected3 = [[0, 0, 0], [0, 1, 1]]
        print("Test 3 Passed" if result3 == expected3 else f"Test 3 Failed: {result3}")

        # Test case 4
        image4 = [[1]]
        sr4, sc4, color4 = 0, 0, 2
        result4 = self.floodFill(image4, sr4, sc4, color4)
        expected4 = [[2]]
        print("Test 4 Passed" if result4 == expected4 else f"Test 4 Failed: {result4}")

        # Test case 5
        image5 = [[1, 1], [1, 0]]
        sr5, sc5, color5 = 0, 0, 1
        result5 = self.floodFill(image5, sr5, sc5, color5)
        expected5 = [[1, 1], [1, 0]]  # No change because the color matches sourcepixl
        print("Test 5 Passed" if result5 == expected5 else f"Test 5 Failed: {result5}")

# Instantiate the solution and run tests
solution = Solution()
solution.test()
