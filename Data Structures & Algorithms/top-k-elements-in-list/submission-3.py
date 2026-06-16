class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        heap = []
        for item,freq in count.items():
            heapq.heappush(heap,[-freq,item])
        res = []
        for i in range(k):
            _,item = heapq.heappop(heap)
            res.append(item)
        return res