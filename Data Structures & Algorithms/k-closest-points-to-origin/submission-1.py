class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_coor = [[x**2+y**2,i,x,y] for i,(x,y) in enumerate(points)]
        heapq.heapify(dis_coor)
        res = [[0,0] for _ in range(k)]
        for i in range(k):
            dis,ind,x,y = heapq.heappop(dis_coor)
            res[i] = [x,y]
        return res