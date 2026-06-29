class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<1:
            return []
        char = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        res = []
        length = len(digits)
        def backtrack(cur,index):
            if index==length:
                res.append(cur)
                return
            for c in char[digits[index]]:
                backtrack(cur+c,index+1)
        backtrack('',0)
        return res