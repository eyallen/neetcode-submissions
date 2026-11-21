class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        n = len(prices)
        if n <= 1:
            return 0

        min_seen = prices[0]
        for i in range(1, n):
            profit = prices[i] - min_seen
            max_profit = max(max_profit, profit)

            if prices[i] < min_seen:
                min_seen = prices[i]

        return max_profit