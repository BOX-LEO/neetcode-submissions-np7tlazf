class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target>nums[-1]:
            return -1
        l,r = 0,len(nums)-1
        while l+1<r:
            mid = int((r-l)/2)+l
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid
            elif nums[mid]<target:
                l=mid
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        return -1