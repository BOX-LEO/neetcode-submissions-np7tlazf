class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        result =[]
        if digits=="":
            return []

        def dfs(res:str,n:int):
            if n == len(digits):
                result.append(res)
                return
            chars = char[int(digits[n])]
            for c in chars:
                res+=c
                dfs(res,n+1)
                res= res[:-1]
        dfs("",0)
        return result
        