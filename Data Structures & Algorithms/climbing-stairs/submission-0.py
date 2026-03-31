class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        l=2
        r = 3
        i = 4 
        while i<=n:
            i,l,r = i+1,r,l+r
        return r