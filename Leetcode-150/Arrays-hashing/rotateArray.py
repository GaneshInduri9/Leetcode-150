from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k > n:
            k = k % n

        def reverse(l: int, h: int):
            while l < h:
                nums[l], nums[h] = nums[h], nums[l]
                l += 1
                h -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


def test():
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    print(nums)


if __name__ == "__main__":
    test()
