class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        else:
            return max(self.helper(nums[1:]),self.helper(nums[:-1]))
           
        
    def helper(self,nums):
        length = len(nums)
        if length<3:
            return max(nums)
        rob1,rob2,rob3 = nums[0],nums[1],nums[2]+nums[0]
        i=3
        while i<length:
            rob1,rob2,rob3,i = rob2,rob3,max(rob1,rob2)+nums[i],i+1
        return max(rob3,rob2)
