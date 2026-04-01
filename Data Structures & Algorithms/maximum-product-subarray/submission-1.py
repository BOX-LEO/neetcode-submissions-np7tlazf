class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max,_min = 1,1
        res = max(nums)
        for n in nums:
            _max,_min = max(_max*n,_min*n,n), min(_max*n,_min*n,n)
            res = max(res,_max)
        return res