class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        start = prices[0]
        profit = 0
        for p in prices:
            if p < start:
                start = p
            else:
                new_profit = p - start
                if new_profit > profit:
                    profit = new_profit
            
        return profit