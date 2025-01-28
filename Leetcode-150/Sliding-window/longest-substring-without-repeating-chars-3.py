class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        l = 0
        max_len = 0

        for r in range(n):
            if s[r] in seen:

                # make sure we have seen it in the same window
                # we can delete the previous elements but we can
                # do that without that as well by making sure where
                # it was seen in the same window.
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len


def test():
    sol = Solution()
    res = sol.lengthOfLongestSubstring("cadbzabcd")
    print(res)


if __name__ == "__main__":
    test()
