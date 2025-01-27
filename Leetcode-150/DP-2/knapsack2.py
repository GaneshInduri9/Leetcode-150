"""
    Assume a theif wants to steal some money from a house and he has bunch of items and each item has a value
    and weight correspoding to that and also he has a bag of weight say capacity Note: we can pick each
    item mutliple times, now we wanna maximise the amount we can steal while not exceeding the capacity.
"""

from typing import List


class Solution:
    def knapsacktwoMemo(self, val: List, wt: List, knapsack: int) -> int:
        n = len(wt)

        def f(i, W):
            # Base if we are at zero we can only steal if the wt[0] < W
            if i == 0:
                return (W // wt[0]) * val[0]

            # if we don't take we move with same weight
            notTake = 0 + f(i - 1, W)

            # if we take we stay at same position try picking again
            take = 0
            if wt[i] <= W:
                take = val[i] + f(i, W - wt[i])

            return max(take, notTake)

        return f(n - 1, knapsack)

    def knapsacktwoTab(self, val: List, wt: List, knapsack: int) -> int:
        n = len(wt)
        dp = [[-1 for _ in range(knapsack + 1)] for i in range(n)]

        for w in range(knapsack + 1):
            dp[0][w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(knapsack + 1):
                notTake = 0 + dp[i - 1][w]
                take = 0
                if wt[i] <= w:
                    take = val[i] + dp[i][w - wt[i]]
                dp[i][w] = max(take, notTake)

        return dp[n - 1][knapsack]


def test():
    sol = Solution()
    res = sol.knapsacktwoMemo([40, 30, 50], [3, 2, 2], 5)
    print(res)
    res2 = sol.knapsacktwoTab([40, 30, 50], [3, 2, 2], 5)
    print(res2)


if __name__ == "__main__":
    test()
