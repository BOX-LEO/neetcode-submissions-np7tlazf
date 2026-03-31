class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n==2:
            return 2
        ways1=1
        ways2=2
        for i in range(2,n):
            ways1,ways2 = ways2, ways1+ways2
        return ways2