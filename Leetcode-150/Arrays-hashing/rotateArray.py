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

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        0 ...... low-1  low ...... mid -1  mid ......high high+1 ......n
          0000000           111111             unsorted     222222
        """

        l = 0
        m = 0
        n = len(nums)
        h = n - 1

        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h = h - 1


def test():
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    print(nums)


if __name__ == "__main__":
    test()
