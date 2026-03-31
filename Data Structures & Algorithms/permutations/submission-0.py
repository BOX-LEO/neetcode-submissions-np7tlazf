class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(cand, temp):
            if cand == []:
                result.append(temp.copy())
            for i in range(len(cand)):
                temp.append(cand[i])
                cand_temp = [x for n, x in enumerate(cand) if n!=i]
                dfs(cand_temp,temp)
                temp.pop()
        dfs(nums,[])
        return result