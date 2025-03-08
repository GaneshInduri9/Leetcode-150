class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                return f(i - 1, j - 1)

            delete = 1 + f(i - 1, j)
            insert = 1 + f(i, j - 1)
            replace = 1 + f(i - 1, j - 1)
            dp[i][j] = min(delete, insert, replace)
            return dp[i][j]

        return f(n - 1, m - 1)

    def minDistanceTb(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = 1 + dp[i - 1][j]
                    replace = 1 + dp[i - 1][j - 1]
                    insert = 1 + dp[i][j - 1]
                    dp[i][j] = min(delete, replace, insert)

        return dp[n][m]


def test():
    s = "horse"
    t = "ros"

    sol = Solution()
    res = sol.minDistanceTb(s, t)
    print(res)


if __name__ == "__main__":
    test()
