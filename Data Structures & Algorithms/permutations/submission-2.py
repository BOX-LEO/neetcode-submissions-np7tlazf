class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(cur,seen):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            for i in nums:
                if i not in seen:
                    cur.append(i)
                    seen.add(i)
                    backtrack(cur,seen)
                    seen.remove(i)
                    cur.pop()
        backtrack([],set())
        return res