class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        def backtrack(cur,level):
            if level == l:
                res.append(cur.copy())
                return
            backtrack(cur,level+1)
            cur.append(nums[level])
            backtrack(cur,level+1)
            cur.pop()
        backtrack([],0)

        return res