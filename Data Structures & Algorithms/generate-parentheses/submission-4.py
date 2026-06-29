class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(l: int, r: int):
            if l == r == n:
                res.append("".join(path))
                return

            if l < n:
                path.append("(")
                backtrack(l + 1, r)
                path.pop()

            if r < l:
                path.append(")")
                backtrack(l, r + 1)
                path.pop()

        backtrack(0, 0)
        return res
