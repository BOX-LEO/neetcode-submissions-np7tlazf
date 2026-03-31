class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topk = nums
        if len(self.topk)<k:
            self.topk = self.topk+[-1001]*(k-len(self.topk))
        heapq.heapify(self.topk)
        while len(self.topk)>k:
            heapq.heappop(self.topk)
        
        

    def add(self, val: int) -> int:
       heapq.heappushpop(self.topk,val)
       return self.topk[0]
