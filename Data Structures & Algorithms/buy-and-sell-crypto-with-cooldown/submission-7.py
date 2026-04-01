class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold,sell,rest = -prices[0],0,0
        for p in prices[1:]:
            hold,sell,rest= max(hold,rest-p), p+hold, max(sell,rest)
        return max(sell,rest)
            



