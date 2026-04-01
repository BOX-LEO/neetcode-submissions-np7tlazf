class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s)==1:
            return 1
        # how may ways if current character 
        # decode by it self or with previous character
        dp1,dp2 = 1,0 

        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] =='1' or s[i-1] =='2':
                    dp2,dp1 = dp1,0
                else:
                    return 0
            elif s[i] in ['1','2','3','4','5','6']:
                if s[i-1]=='0':
                    dp1,dp2 = dp2,0
                elif s[i-1] =='1' or s[i-1] =='2':
                    dp1,dp2= dp1+dp2,dp1
                else: 
                    dp1,dp2 = dp1+dp2,0
            else:
                if s[i-1]=='0':
                    dp1,dp2 = dp2,0
                elif s[i-1] =='1':
                    dp1,dp2= dp1+dp2,dp1
                else: 
                    dp1,dp2 = dp1+dp2,0

        return dp1+dp2