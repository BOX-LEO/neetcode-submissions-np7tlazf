class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        nums.sort()
        def dfs(ind,temp):
            if ind==length:
                result.append(temp.copy())
                return
            temp.append(nums[ind])
            dfs(ind+1,temp)
            temp.pop()
            while ind+1<length and nums[ind+1]==nums[ind]:
                ind+=1
            dfs(ind+1,temp)
        dfs(0,[])
        return result