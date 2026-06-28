class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur=[],total=0,level=0):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target:
                return
            for i,n in enumerate(nums[level:]):
                cur.append(n)
                total+=n
                backtrack(cur,total,level+i)
                cur.pop()
                total-=n

        backtrack()
        return res