class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = dp[1] = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] in {'1','2'}:
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            elif s[i] in {'1','2','3','4','5','6'}:
                dp[i+1]+=dp[i]
                if s[i-1] in {'1','2'}:
                    dp[i+1]+=dp[i-1]
            elif s[i] in {'7','8','9'}:
                dp[i+1]+=dp[i]
                if s[i-1] == '1':
                    dp[i+1]+=dp[i-1]

        return dp[-1]