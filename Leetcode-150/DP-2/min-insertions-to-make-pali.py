class Solution:
    def minInsertions(self, s: str) -> int:

        # min_insertions = n - longestpsubstring
        n = len(s)
        t = s[::-1]
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return n - dp[n][n]


def test():
    s = Solution()
    res = s.minInsertions("acabca")
    print(res)


if __name__ == "__main__":
    test()
