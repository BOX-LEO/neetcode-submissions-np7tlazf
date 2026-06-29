class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combination(a,b):
            b = min(b,a-b)
            top = 1
            bot = 1
            for i in range(b):
                top*=a
                bot*=i+1
                a-=1
            return top//bot
        return combination(m+n-2,n-1)

