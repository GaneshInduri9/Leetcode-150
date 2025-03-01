class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def f(i, j):
            if i < 0 or j < 0:
                return 0
            # match
            if text1[i] == text2[j]:
                memo[i][j] = 1 + f(i - 1, j - 1)
                return 1 + f(i - 1, j - 1)

            # if solved return
            if memo[i][j] != -1:
                return memo[i][j]

            # nonMatch
            memo[i][j] = 0 + max(f(i - 1, j), f(i, j - 1))
            return 0 + max(f(i - 1, j), f(i, j - 1))

        return f(n - 1, m - 1)

    def longestCommonSubsequenceTab(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j - 1])

        return dp

    def longestComSubPrint(self, s, t):
        dp = self.longestCommonSubsequenceTab(s, t)

        i = len(s)
        j = len(t)

        res = []
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res.append(s[i - 1])
                i -= 1
                j -= 1

            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        return "".join(reversed(res))


def test():
    sol = Solution()
    s1 = "acd"
    s2 = "ecd"
    res1 = sol.longestCommonSubsequence(s1, s2)
    assert res1 == 2, "Test case failed"

    res3 = sol.longestComSubPrint(s1, s2)

    print(res3)


if __name__ == "__main__":
    test()
