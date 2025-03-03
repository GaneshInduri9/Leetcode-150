class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        maxLen = 0

        for i in range(n):

            # odd case
            r = i
            l = i

            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    start = l
                    maxLen = r - l + 1
                r += 1
                l -= 1

            # even case
            r = i + 1
            l = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    start = l
                    maxLen = r - l + 1
                r += 1
                l -= 1

        return s[start : start + maxLen]


def test():
    s = Solution()
    even = s.longestPalindrome("baabght")
    odd = s.longestPalindrome("babab")

    print(even)
    print(odd)


if __name__ == "__main__":
    test()
