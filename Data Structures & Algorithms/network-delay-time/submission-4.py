class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for source,target,time in times:
            graph[source-1].append((target,time))
        
        dist = [float('inf')]*n
        dist[k-1] = 0
        heap = [(0,k)] # distance, index
        while heap:
            d,node = heapq.heappop(heap)
            if d>dist[node-1]:
                continue
            for n, t in graph[node-1]:
                new_dist = d+t
                if new_dist<dist[n-1]:
                    dist[n-1]=new_dist
                    heapq.heappush(heap,(new_dist,n))
        max_dist = max(dist)
        if max_dist == float('inf'):
            return -1
        else:return max_dist

