from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        maxP = 0
        curMin = prices[0]

        for i in range(1, n):
            if prices[i] > curMin:
                maxP = max(maxP, prices[i] - curMin)

            if prices[i] < curMin:
                curMin = prices[i]

        return maxP


def test():
    sol = Solution()
    prices = [2, 3, 9, 5, 1]
    res = sol.maxProfit(prices)
    print(res)


if __name__ == "__main__":
    test()
