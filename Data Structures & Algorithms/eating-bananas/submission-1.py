class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)

        import math
        def calculate_hour(piles:List[int],rate):
            result = 0
            for b in piles:
                result+=math.ceil(b/rate)
            # print(result)
            return result

        l,r = 1,max(piles)
        while l+1<r:
            mid = int((r-l)/2)+l
            # print(mid)
            if calculate_hour(piles,mid)>h:
                # print('here')
                l = mid
            else:
                r=mid
            # print(l,r)
        
        if not calculate_hour(piles,l)>h:
            return l
        else: return r
        
        