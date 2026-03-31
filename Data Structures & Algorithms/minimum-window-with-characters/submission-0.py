class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = Counter(list(t))
        cur_s = defaultdict(int) # count the current s
        min_length = float('inf')
        res = ''
        got = 0
        for r in range(len(s)):
            cur_s[s[r]]+=1
            if s[r] in count and cur_s[s[r]]<=count[s[r]]:
                got+=1
            # check if current window contain target
            # move l forward
            while got == len(t):
                if s[l] in count and cur_s[s[l]]==count[s[l]]:
                    if min_length>r-l+1:
                        min_length = r-l+1
                        res = s[l:r+1]
                    got-=1
                cur_s[s[l]]-=1
                l+=1
        return res
