"""
    You are given an integer array prices where prices[i] is the price
    of NeetCoin on the ith day.You may choose a single day to buy one 
    NeetCoin and choose a different day in the future to sell it. Return
    the maximum profit you can achieve. You may choose to not make any 
    transactions, in which case the profit would be 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices:
            return 0  # Handle edge case where prices list is empty
        min_price = prices[0]
        n = len(prices)
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit

def test_maxProfit():
    solution = Solution()

    # Test Case 1: Typical case with a profit
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5, f"Test Case 1 Failed: {solution.maxProfit(prices)}"

    # Test Case 2: Prices always decreasing (no profit possible)
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0, f"Test Case 2 Failed: {solution.maxProfit(prices)}"

    # Test Case 3: Prices constant (no profit possible)
    prices = [3, 3, 3, 3, 3]
    assert solution.maxProfit(prices) == 0, f"Test Case 3 Failed: {solution.maxProfit(prices)}"

    # Test Case 4: Single day (no transactions possible)
    prices = [5]
    assert solution.maxProfit(prices) == 0, f"Test Case 4 Failed: {solution.maxProfit(prices)}"

    # Test Case 5: Large profit with fluctuating prices
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.maxProfit(prices) == 9, f"Test Case 5 Failed: {solution.maxProfit(prices)}"

    # Test Case 6: Profit possible only in the middle of the array
    prices = [10, 7, 5, 3, 6, 8, 4]
    assert solution.maxProfit(prices) == 5, f"Test Case 6 Failed: {solution.maxProfit(prices)}"

    # Test Case 7: Empty prices list (edge case)
    prices = []
    assert solution.maxProfit(prices) == 0, f"Test Case 7 Failed: {solution.maxProfit(prices)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_maxProfit()
