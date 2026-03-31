class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        print(nums_set)
        return not len(nums_set) == len(nums)

         