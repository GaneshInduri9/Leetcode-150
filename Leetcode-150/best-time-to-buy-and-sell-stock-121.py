"""
    You are given an integer array prices where prices[i] is the price
    of NeetCoin on the ith day.You may choose a single day to buy one 
    NeetCoin and choose a different day in the future to sell it. Return
    the maximum profit you can achieve. You may choose to not make any 
    transactions, in which case the profit would be 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        min_price = prices[0]
        n = len(prices)
        for i in range(1,n):
            max_profit = max(max_profit, prices[i] - min_price)
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit