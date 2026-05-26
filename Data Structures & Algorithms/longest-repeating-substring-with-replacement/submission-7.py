from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        for i in range(len(s)):
            count[s[i]]+=1
            cur = i-l+1
            if cur - max(count.values())<=k:
                res = max(res,cur)
            else:
                count[s[l]]-=1
                l+=1
        return res


