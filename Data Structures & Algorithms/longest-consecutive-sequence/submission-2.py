class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        length=0
        max_length=0
        for i in numset:
            if i-1 not in numset:
                length=1
                while i+1 in numset:
                    length+=1
                    i+=1
                    
                if length > max_length:
                    max_length=length
            
        return max_length

                