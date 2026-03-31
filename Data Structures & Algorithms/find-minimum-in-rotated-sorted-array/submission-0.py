class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        l,r = 0,len(nums)-1

        while l+1<r:
            mid = int((r-l)/2)+l
            print(nums[l],nums[mid],nums[r])
            if nums[mid]>nums[l]:
                l=mid
            elif nums[mid]<nums[r]:
                r = mid
        return min(nums[l],nums[r])
        