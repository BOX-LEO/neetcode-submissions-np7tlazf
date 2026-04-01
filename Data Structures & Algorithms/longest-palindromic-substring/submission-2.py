class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def expend(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j-1
        best_l,best_r = 0,0
        for i in range(len(s)-1):
            # odd:
            l,r = expend(i,i)
            if r-l+1>best_r-best_l+1:
                best_l,best_r = l,r
            # even:
            l,r = expend(i,i+1)
            if r-l+1>best_r-best_l+1:
                best_l,best_r = l,r
        return s[best_l:best_r+1]

