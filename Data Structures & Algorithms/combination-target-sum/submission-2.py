class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur,cur_sum,idx):
            if cur_sum==target:
                res.append(cur.copy())
                return
            for i,n in enumerate(nums[idx:]):
                if n<=target-cur_sum:
                    cur.append(n)
                    backtrack(cur,cur_sum+n,idx+i)
                    cur.pop()
        backtrack([],0,0)
        return res

                
