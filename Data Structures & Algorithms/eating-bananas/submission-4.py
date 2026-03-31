class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r =1, max(piles)
        def get_hour(k):
            hour = 0
            for p in piles:
                hour+= p//k
                if p%k>0:
                    hour+=1
            return hour
        while l<=r:
            mid = l+(r-l)//2
            hour = get_hour(mid)
            if hour<=h:
                r=mid-1
            else:
                l = mid+1
        return l