class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = len(cost)
        if steps<2:
            return 0
        s_2,s_1 = 0,0
        i = 2
        while i<=steps:
            s_2, s_1,i =s_1, min(s_2+cost[i-2],s_1+cost[i-1]),i+1
        return s_1
