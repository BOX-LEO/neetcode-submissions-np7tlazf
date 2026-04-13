class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2 = len(s1),len(s2)
        if l1+l2!=len(s3):
            return False
        dp = [[False]*(l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        for i in range(1,l1+1):
            dp[0][i] = dp[0][i-1] and s1[i-1]==s3[i-1]
        for i in range(1,l2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1] ==s3[i-1]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                o1 = dp[j-1][i] and s2[j-1]==s3[i+j-1]
                o2 = dp[j][i-1] and s1[i-1]==s3[i+j-1]
                dp[j][i] = o1 or o2
        return dp[l2][l1]