class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        dp1 = 1
        dp2 = 2
        for _ in range(n-2):
            dp1,dp2 = dp2,dp1+dp2
        return dp2
