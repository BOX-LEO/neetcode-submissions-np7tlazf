class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur,level):
            if level ==len(nums):
                res.append(cur.copy())
                return
            else:
                cur.append(nums[level])
                backtrack(cur,level+1)
                cur.pop()
                backtrack(cur,level+1)
        backtrack([],0)
        return res
                
                