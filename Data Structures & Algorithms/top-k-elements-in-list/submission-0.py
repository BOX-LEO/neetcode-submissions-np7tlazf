class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(set(nums)):
            return [i for i in set(nums)]
        
        dic = {i:0 for i in set(nums)}
        for i in nums:
            dic[i]+=1
        freq = [[] for _ in range(len(nums)+1)]
        for n,f in dic.items():
            freq[f].append(n)
        result = []
        for i in freq[::-1]:
            for n in i:
                result.append(n)
                if len(result)==k:
                    return result
        
