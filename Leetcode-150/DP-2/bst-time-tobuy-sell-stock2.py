from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def f(i, buy):
            if i == n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            profit = 0
            if buy:
                profit = max(-prices[i] + f(i + 1, 0), 0 + f(i + 1, 1))
            else:
                profit = max(prices[i] + f(i + 1, 1), 0 + f(i + 1, 0))
            dp[i][buy] = profit
            return profit

        return f(0, 1)

    def maxProfitDp(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][0] = dp[n][1] = 0

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
                else:
                    profit = max(prices[i] + dp[i + 1][1], 0 + dp[i + 1][0])

                dp[i][buy] = profit

        return dp[0][1]

    def maxProfitSpace(self, prices: List[int]) -> int:
        n = len(prices)
        prev = [0] * 2
        cur = [0] * 2

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[i] + prev[0], 0 + prev[1])
                else:
                    profit = max(prices[i] + prev[1], 0 + prev[0])

                cur[buy] = profit

            prev = cur

        return prev[1]


def test():
    sol = Solution()
    res = sol.maxProfitDp([7, 1, 5, 3, 6, 4])
    print(res)


if __name__ == "__main__":
    test()
