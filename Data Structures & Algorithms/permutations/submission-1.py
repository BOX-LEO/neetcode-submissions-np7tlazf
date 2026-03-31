class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(cand, temp):
            if cand == []:
                result.append(temp.copy())
            for i in range(len(cand)):
                c = cand.pop(0)
                temp.append(c)
                dfs(cand,temp)
                cand.append(c)
                temp.pop()
        dfs(nums,[])
        return result