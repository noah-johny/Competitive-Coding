class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        cp, profit = prices[0], 0

        for i in range(1, size):
            price = prices[i]

            if price < cp:
                cp = price
            elif price - cp > profit:
                profit = price - cp

        return profit