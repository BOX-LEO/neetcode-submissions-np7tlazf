class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            while c in cur_set:
                cur_set.remove(s[l])
                l+=1
            cur_set.add(s[r])
            res = max(res,len(cur_set))
        return res