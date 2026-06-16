class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        for p in prices:
            profit = max(profit,p-cur_min)
            cur_min = min(cur_min,p)
        return profit