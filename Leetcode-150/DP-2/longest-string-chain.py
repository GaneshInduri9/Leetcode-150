from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        dp = [1] * n
        maxi = 1
        for i in range(n):
            for j in range(i):

                if self.compare(words[i], words[j]) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

            maxi = max(maxi, dp[i])

        return maxi

    def compare(self, s1, s2):
        n = len(s1)
        m = len(s2)

        if n != m + 1:
            return False

        i = 0
        j = 0

        while i < n:
            if j < m and s1[i] == s2[j]:
                i += 1
                j += 1

            else:
                i += 1

        if i == n and j == m:
            return True
        else:
            return False


def test():
    sol = Solution()
    res = sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
    print(res)


if __name__ == "__main__":
    test()
