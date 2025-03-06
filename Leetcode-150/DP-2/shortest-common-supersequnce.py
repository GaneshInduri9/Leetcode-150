class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        # len of shortestCommonSupersequence = len(str1) + len(str2) - lcs(s1, s2)
        dp = self.longestCommonSubsequenceTab(str1, str2)
        n = len(str1)
        m = len(str2)
        i = n
        j = m
        ans = []
        while i > 0 and j > 0:

            # when charcters match take only one into account
            if str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1

            # we are moving above then we need to take i into consideration
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans.append(str1[i - 1])
                i -= 1
            # we are moving side then we need to take j into consideration
            else:
                ans.append(str2[j - 1])
                j -= 1

        # we might not finish the DP table completely some make sure we add the rest of the stuff as well
        while i > 0:
            ans.append(str1[i - 1])
            i -= 1
        while j > 0:
            ans.append(str2[j - 1])
            j -= 1

        return "".join(reversed(ans))

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


def test():
    sol = Solution()
    s1 = "brute"
    s2 = "groot"
    # ans = bgruoote
    sol.shortestCommonSupersequence(s1, s2)


if __name__ == "__main__":
    test()
