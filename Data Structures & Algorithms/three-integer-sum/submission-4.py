class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        length = len(nums)
        def twoSum(target,start):
            l,r = start,length-1
            while l<r:
                if nums[l]+nums[r]==target:
                    res.append([-target,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<length and nums[l]==nums[l-1]:
                        l+=1
                    while r>=start and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            twoSum(-nums[i],i+1)
        return res
