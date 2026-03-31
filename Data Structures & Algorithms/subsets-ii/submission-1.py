class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur,level,passed):
            if level == len(nums):
                res.append(cur.copy())
                return
            if nums[level] not in passed:
                cur.append(nums[level])
                backtrack(cur,level+1,passed)
                cur.pop()
                passed.add(nums[level])
                backtrack(cur,level+1,passed)
                passed.remove(nums[level])
            else:
                backtrack(cur,level+1,passed)
        backtrack([],0,set())
        return res