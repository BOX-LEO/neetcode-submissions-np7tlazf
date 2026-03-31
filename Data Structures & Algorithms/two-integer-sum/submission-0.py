class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = [target-i for i in nums]
        for i in range(len(solution)):
            if solution[i] in set(nums):
                j=nums.index(solution[i])
                if i<j:
                    return [i,j]
                elif i>j:
                    return [j,i]
            


