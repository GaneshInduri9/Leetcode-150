class Solution:
    def shortest_distance(self, matrix):
        V = len(matrix)

        # Step 1: Replace -1 with a large value and set diagonal to 0
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == -1:
                    matrix[i][j] = int(1e9)  # Use int to avoid floating point issues
                if i == j:
                    matrix[i][j] = 0

        # Step 2: Floyd-Warshall Algorithm
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # Step 3: Convert large values back to -1 to indicate no path
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == int(1e9):
                    matrix[i][j] = -1


def test():
    sol = Solution()

    # Test Case 1
    matrix = [[0, 3, -1], [2, 0, -1], [-1, 7, 0]]
    sol.shortest_distance(matrix)
    print(matrix)  # Expected: [[0, 3, -1], [2, 0, -1], [-1, 5, 0]]

    # Test Case 2
    matrix = [[0, 4, 8, -1], [4, 0, 2, 6], [8, 2, 0, 3], [-1, 6, 3, 0]]
    sol.shortest_distance(matrix)
    print(matrix)

    # Test Case 3
    matrix = [[0, -1, 3], [-1, 0, -1], [3, -1, 0]]
    sol.shortest_distance(matrix)
    print(matrix)

    # Test Case 4
    matrix = [[0, 5, -1, 10], [-1, 0, 3, -1], [-1, -1, 0, 1], [-1, -1, -1, 0]]
    sol.shortest_distance(matrix)
    print(matrix)


if __name__ == "__main__":
    test()
