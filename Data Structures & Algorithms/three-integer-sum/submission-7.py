class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        def twoSum(part:List[int],target:int)-> List[List[int]]:
            length = len(part)
            l,r = 0,length-1
            while l<r:
                if part[l]+part[r]==target:
                    res.add((-target,part[l],part[r]))
                    l+=1
                    r-=1
                elif part[l]+part[r] > target:
                    r-=1
                else:
                    l+=1

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            twoSum(nums[i+1:],-nums[i])
        output = []
        for i in res:
            output.append(list(i))
        return output

