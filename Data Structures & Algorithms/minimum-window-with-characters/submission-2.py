class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        got = 0
        count_t = Counter(t)
        count_cur = defaultdict(int)
        l = 0
        min_length = float('inf')
        res = ''
        for i in range(len(s)):
            count_cur[s[i]]+=1
            if count_cur[s[i]]<=count_t[s[i]]:
                got+=1
            while got >= len(t):
                if s[l] in count_t and count_cur[s[l]]==count_t[s[l]]:
                    got-=1
                    if i-l+1< min_length:
                        min_length = i-l+1
                        res = s[l:i+1]
                    
                count_cur[s[l]]-=1
                l+=1
        return res
