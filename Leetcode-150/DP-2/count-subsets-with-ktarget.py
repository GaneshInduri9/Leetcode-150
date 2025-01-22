from typing import List

class Solution:
    def findWays(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = [[-1 for _ in range(k + 1)] for _ in range(n)]

        def f(i, cur):
            if cur == 0:
                return 1

            if i == 0:
                if arr[i] == cur:
                    return 1
                return 0

            if memo[i][cur] != -1:
                return memo[i][cur]

            notTake = f(i - 1, cur)
            take = 0
            if arr[i] <= cur:
                take = f(i - 1, cur - arr[i])

            memo[i][cur] = notTake + take
            return memo[i][cur]

        return f(n - 1, k)

    def findWaysTab(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        if arr[0] <= k:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            for target in range(1, k + 1):
                notTake = dp[i - 1][target]
                take = 0
                if arr[i] <= target:
                    take = dp[i - 1][target - arr[i]]

                dp[i][target] = take + notTake

        return dp[n - 1][k]

def test_solution():
    sol = Solution()

    # Test Case 1: Simple Case
    arr = [1, 2, 3]
    k = 4
    assert sol.findWays(arr, k) == 1  # [1, 3]
    assert sol.findWaysTab(arr, k) == 1

    # Test Case 2: No Subset Sums to k
    arr = [2, 4, 6]
    k = 5
    assert sol.findWays(arr, k) == 0
    assert sol.findWaysTab(arr, k) == 0

    # Test Case 3: Single Element Matches k
    arr = [5]
    k = 5
    assert sol.findWays(arr, k) == 1  # [5]
    assert sol.findWaysTab(arr, k) == 1

    # Test Case 4: Larger Array with Multiple Matches
    arr = [1, 2, 2, 3]
    k = 4
    assert sol.findWays(arr, k) == 2  # [1, 3], [2, 2]
    assert sol.findWaysTab(arr, k) == 2

    print("All test cases passed!")

test_solution()

