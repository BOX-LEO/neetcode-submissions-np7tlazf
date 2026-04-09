class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = defaultdict(int)
        count[0]+=1
        for n in nums:
            temp = defaultdict(int)
            for total, c in count.items():
                temp[total+n]+=c
                temp[total-n]+=c
            count = temp
        return count[target]