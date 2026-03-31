class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l+1<r:
            mid = int((r-l)/2)+l
            if nums[mid]==target:
                    return mid

            if nums[l]<nums[r]:
                if nums[mid]>target:
                    r = mid
                else:
                    l=mid
            else:
                if nums[l]<=target:
                    if nums[mid]<nums[l]:
                        r = mid
                    elif nums[mid]<target:
                        l = mid
                    else:
                        r = mid
                else:
                    if nums[mid]>nums[r]:
                        l = mid
                    elif nums[mid]<target:
                        l = mid
                    else:
                        r = mid
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        return -1

