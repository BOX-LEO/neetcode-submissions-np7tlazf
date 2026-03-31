class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def help(money):
            if len(money) ==1:
                return money[0]
            r,nr = money[0],0
            for m in money[1:]:
                r,nr = nr+m,max(r,nr)
            return max(r,nr)
        return max(help(nums[:-1]),help(nums[1:]))