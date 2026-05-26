class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):

            while stack:
                if t>temperatures[stack[-1]]:
                    ind = stack.pop()
                    res[ind] = i-ind
                else:
                    break
            stack.append(i)
        return res