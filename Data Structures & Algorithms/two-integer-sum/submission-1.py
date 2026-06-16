class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = defaultdict(int)
        for i,n in enumerate(nums):
            if target-n not in checked:
                checked[n]=i
            else:
                return [checked[target-n],i]
