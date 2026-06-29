class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        words = set(wordDict)
        for end in range(1,len(s)+1):
            for start in range(end-1,-1,-1):
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break
        return dp[-1]