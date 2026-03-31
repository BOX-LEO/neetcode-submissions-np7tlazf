class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur,left,right):
            if left ==right ==n:
                res.append(cur)
                return
            if left<n:
                backtrack(cur+'(',left+1,right)
            if right<left:
                backtrack(cur+')',left,right+1)
        backtrack('',0,0)
        return res
            
