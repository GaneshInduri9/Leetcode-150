from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def f(i, buy):
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            profit = 0
            if buy:
                profit = max(-prices[i] + f(i + 1, 0), 0 + f(i + 1, 1))
            else:
                profit = max(prices[i] + f(i + 2, 1), 0 + f(i + 1, 0))
            dp[i][buy] = profit
            return profit

        return f(0, 1)

    def maxProfitTab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy == 1:
                    profit = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
                else:
                    profit = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])
                dp[i][buy] = profit

        return dp[0][1]

    def maxProfitSpace(self, prices: List[int]) -> int:
        n = len(prices)
        cur = [0, 0]
        front1 = [0, 0]
        front2 = [0, 0]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy == 0:  # We can buy the stock
                    profit = max(0 + front1[0], -prices[ind] + front1[1])

                if buy == 1:  # We can sell the stock
                    profit = max(0 + front1[1], prices[ind] + front2[0])

                cur[buy] = profit

            # Update the 'front' lists for the next iteration
            front2 = front1.copy()
            front1 = cur.copy()

        return cur[0]


def test():
    sol = Solution()
    res = sol.maxProfitTab([7, 1, 5, 3, 6, 4])
    print(res)


if __name__ == "__main__":
    test()
