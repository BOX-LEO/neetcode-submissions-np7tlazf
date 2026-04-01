class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = m-1+n-1
        if m>n:
            m,n=n,m
        res = 1
        for i in range(1,m):
            res*=steps
            res/=i
            steps-=1
        return int(res)