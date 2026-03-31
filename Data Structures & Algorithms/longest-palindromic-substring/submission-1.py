class Solution:
    def longestPalindrome(self, s: str) -> str:
        def span_Palindrome(s,ind:list,res = '',max_length =0):
            l,r = ind[0],ind[1]
            length = len(s)
            while l>=0 and r<length and s[l]==s[r]:
                # print(s[l:r+1])
                # print(max_length)
                l-=1
                r+=1
            if r-l-1>max_length:
                
                return s[l+1:r],r-l-1
            else:
                return res,max_length
        max_length = 0
        res = ''
        for i in range(len(s)):
            # print('i=',i)
            res,max_length = span_Palindrome(s,[i,i],res,max_length)
        for i in range(len(s)-1):
            res,max_length = span_Palindrome(s,[i,i+1],res,max_length)
        return res