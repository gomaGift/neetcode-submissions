class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = prices[0]

        for sell, price in enumerate(prices[1:]):
            if price < buy:
                buy = price 
            elif price > buy:
                profit = max(profit, price - buy)

        return profit
        