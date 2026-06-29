class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        take = nums[0]
        skip = 0
        for i in range(1,len(nums)):
            take,skip = skip+nums[i],max(take,skip)
        return max(take,skip)