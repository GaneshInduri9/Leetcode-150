from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for o in range(2)] for i in range(n)]

        def f(i, buy, cap):

            if i == n or cap == 0:
                return 0

            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]
            profit = 0
            if buy:
                profit1 = -prices[i] + f(i + 1, 0, cap)
                profit2 = 0 + f(i + 1, 1, cap)
                profit = max(profit1, profit2)
            else:
                profit1 = prices[i] + f(i + 1, 1, cap - 1)
                profit2 = 0 + f(i + 1, 0, cap)
                profit = max(profit1, profit2)

            dp[i][buy][cap] = profit
            return dp[i][buy][cap]

        return f(0, 1, 2)

    def maxProfittab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(3)] for o in range(2)] for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        dp[i][buy][cap] = max(
                            -prices[i] + dp[i + 1][0][cap], dp[i + 1][1][cap]
                        )
                    else:
                        dp[i][buy][cap] = max(
                            prices[i] + dp[i + 1][1][cap - 1], dp[i + 1][0][cap]
                        )

        return dp[0][1][2]

    def maxProfitSpace(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0 for _ in range(3)] for _ in range(2)]
        cur = [[0 for _ in range(3)] for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 0:
                        # We can buy the stock
                        cur[buy][cap] = max(
                            0 + ahead[0][cap], -prices[ind] + ahead[1][cap]
                        )
                    elif buy == 1:
                        # We can sell the stock
                        cur[buy][cap] = max(
                            0 + ahead[1][cap], prices[ind] + ahead[0][cap - 1]
                        )

            ahead = cur  # Update ahead with the current values

        return ahead[0][2]


def test():
    sol = Solution()
    res = sol.maxProfittab([7, 1, 5, 3, 6, 4])
    print(res)


if __name__ == "__main__":
    test()
