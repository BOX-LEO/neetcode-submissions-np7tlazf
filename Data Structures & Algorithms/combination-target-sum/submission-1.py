class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur,cur_sum,ind):
            if cur_sum == target:
                res.append(cur.copy())
                return
            for i,n in enumerate(nums[ind:]):
                if n<=target-cur_sum:
                    cur.append(n)
                    backtrack(cur,cur_sum+n,i+ind)
                    cur.pop()
        backtrack([],0,0)
        return res