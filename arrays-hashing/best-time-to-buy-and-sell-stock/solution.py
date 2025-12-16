from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        profit = -1

        for i in range(len(prices)):
            # find a new minimum price
            if prices[i] < min_price:
                min_price = prices[i]

            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)

        return max_profit