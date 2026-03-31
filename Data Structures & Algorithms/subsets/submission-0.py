class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        def backtrack(res,step):
            if step == length:
                return result.append(res.copy())
            res.append(nums[step])
            backtrack(res,step+1)
            res.pop()
            backtrack(res,step+1)
        backtrack([],0)
        return result