class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cur = defaultdict(int)
        res = 0
        for r in range(len(s)):
            cur[s[r]]+=1
            # no duplicate
            if max(cur.values())==1:
                res = max(res,r-l+1)
            else:
                cur[s[l]]-=1
                l+=1
        return res