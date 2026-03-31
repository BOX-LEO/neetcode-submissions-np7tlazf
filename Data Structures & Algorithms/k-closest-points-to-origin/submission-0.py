class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [[p[0]**2+p[1]**2, p[0], p[1]] for p in points]
        heapq.heapify(minheap)
        print(minheap)
        result = [[0,0]]*k
        for i in range(k):
            _,x,y = heapq.heappop(minheap)
            result[i]=[x,y]
        return result
        