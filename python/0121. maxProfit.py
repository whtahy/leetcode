class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = profit = 0
        for price in enumerate(prices):
            if price < buy:
                buy = price
            elif (p := price - buy) > profit:
                profit = p
        return profit
