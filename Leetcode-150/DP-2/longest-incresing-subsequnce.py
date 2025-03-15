from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1 for _ in range(n + 1)] for i in range(n)]

        def f(i, prevIdx):
            if i == n:
                return 0

            if dp[i][prevIdx + 1] != -1:
                return dp[i][prevIdx + 1]

            pick = 0
            if prevIdx == -1 or nums[i] > nums[prevIdx]:
                pick = 1 + f(i + 1, i)

            notPick = f(i + 1, prevIdx)

            dp[i][prevIdx + 1] = max(pick, notPick)
            return dp[i][prevIdx + 1]

        return f(0, -1)

    def lengthOfLISDp(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0 for _ in range(n + 1)] for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prevIdx in range(i - 1, -2, -1):

                pick = 0
                if prevIdx == -1 or nums[i] > nums[prevIdx]:
                    pick = 1 + dp[i + 1][i + 1]

                notPick = dp[i + 1][prevIdx + 1]

                dp[i][prevIdx + 1] = max(pick, notPick)

        for row in dp:
            print(" ".join(map(str, row)))

        return dp[0][0]

    def lengthOfLISSpace(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


def test():
    sol = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    res = sol.lengthOfLISDp(arr)
    print(res)


if __name__ == "__main__":
    test()
