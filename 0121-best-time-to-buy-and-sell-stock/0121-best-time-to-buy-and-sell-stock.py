class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell<len(prices):
            current_prof = prices[sell] - prices[buy]
            if current_prof > 0:
                max_profit = max(current_prof, max_profit)

            else:
                buy = sell

            sell += 1

        return max_profit