class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = len(cost)
        if stairs<3:
            return min(cost)
        dp = [0]*(stairs+1)
        for i in range(2,stairs+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[stairs]