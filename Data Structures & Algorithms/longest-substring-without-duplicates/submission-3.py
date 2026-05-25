class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[l]!=s[i]:
                    seen.remove(s[l])
                    l+=1
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            res = max(res,i-l+1)
        return res