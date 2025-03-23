from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


def test():
    sol = Solution()
    print(sol.search([7, 8, 9, 1, 2, 3, 4, 5, 6], 1))


if __name__ == "__main__":
    test()
