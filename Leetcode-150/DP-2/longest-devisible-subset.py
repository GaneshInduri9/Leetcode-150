from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n
        nums.sort()
        parent = [-1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

        lis = max(dp)
        endEle = dp.index(lis)

        lis_subset = []
        while endEle != -1:
            lis_subset.append(nums[endEle])
            endEle = parent[endEle]

        return lis_subset


def test():
    s = Solution()
    res = s.largestDivisibleSubset([1, 2, 3])
    print(res)


if __name__ == "__main__":
    test()
