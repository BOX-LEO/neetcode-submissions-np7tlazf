class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles,speed):
            hour = 0
            for p in piles:
                hour+=math.ceil(p/speed)
            return hour
        
        if len(piles)>h:
            return -1
        left,right = 1, max(piles)
        while left<=right:
            mid = left+(right-left)//2
            if hours(piles,mid)<=h:
                right = mid -1
            else:
                left = mid+1
        return left
        