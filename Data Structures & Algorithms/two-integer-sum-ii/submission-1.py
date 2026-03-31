class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end = len(numbers)-1
        while start<end:
            if target - numbers[start] in numbers:
                end = numbers.index(target - numbers[start])
                return [start+1,end+1]
            else:
                start+=1
        