class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(candidate):
            if len(candidate)==1:
                return True
            l,r = 0,len(candidate)-1
            while l<=r and candidate[l]==candidate[r]:
                l+=1
                r-=1
            return r<l
        res = []
        def backtrack(cur,rem):
            if rem=='':
                res.append(cur.copy())
                return
            for i in range(len(rem)):
                if ispalindrome(rem[:i+1]):
                    cur.append(rem[:i+1])
                    backtrack(cur,rem[i+1:])
                    cur.pop()
        backtrack([],s)
        return res

