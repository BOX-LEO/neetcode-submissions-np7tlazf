class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        for p in prices:
            if p<=cur_min:
                cur_min = p
            else:
                profit = max(profit,p-cur_min)

        return profit