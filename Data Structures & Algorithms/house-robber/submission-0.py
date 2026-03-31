class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <3:
            return max(nums)
        s_3,s_2,s_1 = nums[0],nums[1],nums[2]+nums[0]
        i = 3
        while i<length:
           s_3,s_2, s_1,i = s_2,s_1, max(s_2,s_3)+nums[i],i+1
        
        return max(s_1,s_2)

