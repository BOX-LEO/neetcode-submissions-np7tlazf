class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        res = 0

        heap = [(0,0)]
        visited = set()
        while heap:
            distance,index = heapq.heappop(heap)
            if index in visited:
                continue
            visited.add(index)
            res+=distance
            for i in range(length):
                if i not in visited:
                    dist = abs(points[index][0]-points[i][0])+abs(points[index][1]-points[i][1])
                    heapq.heappush(heap,(dist,i))
        return res
