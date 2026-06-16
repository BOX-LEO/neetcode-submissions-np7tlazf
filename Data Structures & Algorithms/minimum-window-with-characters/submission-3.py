from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = Counter(t)
        cur = defaultdict(int)
        got = 0
        required = len(t)
        l = 0
        res = ""
        for r in range(len(s)):
            c = s[r]
            cur[c] += 1
            if cur[c] <= need[c]:
                got += 1
            while got == required:
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]

                to_remove = s[l]
                cur[to_remove] -= 1

                if to_remove in need and cur[to_remove] < need[to_remove]:
                    got -= 1

                l += 1

        return res

