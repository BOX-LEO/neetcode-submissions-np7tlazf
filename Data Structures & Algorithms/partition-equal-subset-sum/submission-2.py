class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1:
            return False
        target = total//2

        dp = [False]*(target+1)
        dp[0] = True
        for n in nums:
            for i in range(target,n-1,-1):
                if dp[i-n]:
                    dp[i]=True
                if dp[target]:
                    return True

        return dp[-1]