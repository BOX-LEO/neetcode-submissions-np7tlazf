class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(cur,level,passed):
            if level==len(nums):
                res.append(cur.copy())
                return
            if nums[level] in passed:
                backtrack(cur,level+1,passed)
            else:
                cur.append(nums[level])
                backtrack(cur,level+1,passed)
                cur.pop()
                passed.add(nums[level])
                backtrack(cur,level+1,passed)
                passed.remove(nums[level])
        backtrack([],0,set())
        return res
        