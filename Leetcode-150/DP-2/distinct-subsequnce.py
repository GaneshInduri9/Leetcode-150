class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = f(i - 1, j - 1) + f(i - 1, j)
                return dp[i][j]
            dp[i][j] = f(i - 1, j)
            return dp[i][j]

        return f(len(s) - 1, len(t) - 1)

    def numDistinctTb(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


def test():
    sol = Solution()
    s1 = "babgbag"
    s2 = "bag"
    res1 = sol.numDistinctTb(s1, s2)
    assert res1 == 5, "Test case failed"
    print("Success")


if __name__ == "__main__":
    test()
