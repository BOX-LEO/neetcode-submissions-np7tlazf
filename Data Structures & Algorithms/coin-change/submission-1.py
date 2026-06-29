class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for i in range(amount):
            if dp[i]!=float('inf'):
                for avilable in coins:
                    new_amount = i+avilable
                    if new_amount>amount:
                        break
                    dp[new_amount] = min(dp[new_amount],dp[i]+1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]