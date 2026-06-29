class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length<2:
            return 0
        c1,c2 = 0,0
        for i in range(2,length+1):
            c1,c2 = c2,min(c1+cost[i-2],c2+cost[i-1])
        return c2
        