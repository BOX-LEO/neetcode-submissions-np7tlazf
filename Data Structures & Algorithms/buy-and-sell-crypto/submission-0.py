class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        res = 0
        for p in prices:
            if p<=cur_min:
                cur_min = p
            else:
                res = max(res,p-cur_min)
        return res