class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(target,nums,res):
            if target == 0:
                result.append(res.copy())
            for i,n in enumerate(nums):
                if n <= target:
                    res.append(n)
                    dfs(target-n,nums[i:],res)
                    res.pop()
        dfs(target,nums,[])
        return result
        
        
