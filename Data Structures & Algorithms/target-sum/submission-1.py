class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = defaultdict(int)
        count[0]=1
        for n in nums:
            temp = defaultdict(int)
            for k in count.keys():
                temp[k+n]+=count[k]
                temp[k-n]+=count[k]
            count = temp
        return count[target]