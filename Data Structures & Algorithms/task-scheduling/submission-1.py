class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [-i for i in list(count.values())]
        heapq.heapify(freq)
        max_freq = -heapq.heappop(freq)
        idel = n*(max_freq-1)
        while freq and idel>0:
            next_freq = -heapq.heappop(freq)
            idel-= min(next_freq,max_freq-1)
        if idel<0:
            idel = 0
        return idel+len(tasks)