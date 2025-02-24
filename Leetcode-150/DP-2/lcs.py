"Longest common subsequence"


class Solution:
    def longestCommonSubsequnce(self, s, t):

        n = len(s)
        m = len(t)
        memo = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):
            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            if s[i] == t[j]:
                memo[i][j] = 1 + f(i - 1, j - 1)
                return memo[i][j]
            memo[i][j] = 0 + max(f(i - 1, j), f(i, j - 1))
            return memo[i][j]

        return f(n - 1, m - 1)

    def tabulationLcs(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 0
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]


def test():
    s = Solution()
    res = s.tabulationLcs("acd", "ced")
    print(res)


if __name__ == "__main__":
    test()
