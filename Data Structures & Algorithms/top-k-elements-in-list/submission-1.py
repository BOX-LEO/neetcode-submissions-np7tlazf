class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n]+=1
        res_list = [[-freq,i,key] for i,(key,freq) in enumerate(counts.items())]
        heapq.heapify(res_list)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(res_list)[2])
        return res