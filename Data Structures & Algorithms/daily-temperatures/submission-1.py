class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = []
        res = [0]*len(temperatures)
        for n,T in enumerate(temperatures):
            while len(t)>0 and T >t[-1][1]:
                i,tem = t.pop()
                res[i]=n-i
            t.append((n,T))
        return res
