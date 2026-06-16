class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        def twoSum(part:List[int],target:int)-> List[List[int]]:
            length = len(part)
            l,r = 0,length-1
            while l<r:
                if part[l]+part[r]==target:
                    res.append([-target,part[l],part[r]])
                    l+=1
                    r-=1
                    while l<length and part[l]==part[l-1]:
                        l+=1
                    while r>=0 and part[r]==part[r+1]:
                        r-=1
                elif part[l]+part[r] > target:
                    r-=1
                else:
                    l+=1

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            twoSum(nums[i+1:],-nums[i])
        return res
