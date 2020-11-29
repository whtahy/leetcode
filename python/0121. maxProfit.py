class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = math.inf
        for price in prices:
            if price < buy:
                buy = price
            elif (p := price - buy) > profit:
                profit = p
        return profit
