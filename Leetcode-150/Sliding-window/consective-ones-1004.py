from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxlen,
        max_len = 0
        n = len(nums)
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros > k:
                    break
                else:
                    max_len = max(max_len, j - i + 1)
        return max_len

    def longestOnesSlidingWindow(self, nums: List[int], k: int) -> int:
        # maxlen,
        max_len = 0
        n = len(nums)
        l = 0
        r = 0
        zeros = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l = l + 1
            max_len = max(max_len, r - l + 1)
            r = r + 1
        return max_len

    def longestOnesSlidingWindowOptimal(self, nums: List[int], k: int) -> int:
        # maxlen,
        max_len = 0
        n = len(nums)
        l = 0
        r = 0
        zeros = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l = l + 1
            if zeros <= k:
                max_len = max(max_len, r - l + 1)
            r = r + 1
        return max_len


def test():
    sol = Solution()

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    res = sol.longestOnes(nums, k)
    assert res == 10, "Test case failed"
    res2 = sol.longestOnesSlidingWindow(nums, k)
    assert res2 == 10, "Test case failed"
    print("Test cases Done")


if __name__ == "__main__":
    test()
