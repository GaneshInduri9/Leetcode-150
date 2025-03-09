class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        dp = [[-1 for i in range(m)] for j in range(n)]

        def f(i, j):

            if i < 0 and j < 0:
                return True

            if i < 0 and j >= 0:
                for index in range(j + 1):
                    if p[index] != "*":
                        return False
                return True

            if j < 0 and i >= 0:
                return False

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or p[j] == "?":
                dp[i][j] = f(i - 1, j - 1)
                return f(i - 1, j - 1)

            if p[j] == "*":
                dp[i][j] = f(i, j - 1) or f(i - 1, j)
                return dp[i][j]

            dp[i][j] = False
            return False

        return f(n - 1, m - 1)


def test():
    sol = Solution()
    res = sol.isMatch("abcfgde", "ab*de")
    print(res)


if __name__ == "__main__":
    test()
