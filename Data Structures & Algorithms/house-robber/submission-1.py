class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        norob = 0

        for n in nums:
            rob, norob = norob + n, max(rob, norob)

        return max(rob, norob)
        