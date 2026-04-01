class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sell = 0
        rest = 0
        for p in prices[1:]:
            print(hold,sell,rest)
            p_hold = hold
            p_sell = sell
            p_rest = rest
            hold = max(p_hold,p_rest-p)
            sell = p+p_hold
            rest = max(p_sell,p_rest)
        return max(sell,rest)
            



