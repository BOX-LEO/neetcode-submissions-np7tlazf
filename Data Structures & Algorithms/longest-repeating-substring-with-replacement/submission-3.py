class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            cur_length = r-l+1
            if cur_length - max(count.values())<=k:
                res = max(res,cur_length)
            else:
                count[s[l]]-=1
                if count[s[l]] == 0:
                    del count[s[l]]
                    l+=1
                    continue
                l+=1
        return res