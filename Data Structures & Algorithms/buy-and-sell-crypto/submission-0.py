class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        low = prices[0]
        for price in prices:
            profit = price - low
            if profit < 0:
                low = price
            best_profit = max(best_profit, profit)
        return best_profit

