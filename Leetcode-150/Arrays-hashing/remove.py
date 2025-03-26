from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                nums[i] = -1

        k = 0
        for num in nums:
            if num == -1:
                continue

            nums[k] = num
            k = k + 1

        return k


def test():
    sol = Solution()
    res = sol.removeElement([3, 2, 2, 3], 3)
    print(res)


if __name__ == "__main__":
    test()
