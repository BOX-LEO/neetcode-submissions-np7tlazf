class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        no_0_product = 1
        count_0 = 0
        for i in nums:
            if i==0:
                count_0+=1
            else:
                no_0_product=no_0_product*i
        if count_0>1:
            return [0]*len(nums)
        elif count_0==1:
            result = []
            for i in nums:
                if i!=0:
                    result.append(0)
                else:
                    result.append(no_0_product)
        else:
            result=[]
            for i in nums:
                result.append(int(no_0_product/i))
        return result
        
        