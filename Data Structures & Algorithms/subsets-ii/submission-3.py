class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        def backtrack(cur,index,skip):
            if index ==length:
                res.append(cur.copy())
                return
            temp = nums[index]
            if temp in skip:
                backtrack(cur,index+1,skip)
            else:
                cur.append(nums[index])
                backtrack(cur,index+1,skip)
                cur.pop()
                skip.add(nums[index])
                backtrack(cur,index+1,skip)
                skip.remove(nums[index])
        backtrack([],0,set())
        return res
