class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def get_p(stack,l,r):
            if l==r==n:
                res.append(''.join(stack))
            if l<n:
                stack.append('(')
                get_p(stack,l+1,r)
                stack.pop()
            if r<l:
                stack.append(')')
                get_p(stack,l,r+1)
                stack.pop()
        get_p(['('],1,0)
        return res
    