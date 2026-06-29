class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,c in flights:
            graph[s].append((d,c))
        dist = [[float('inf')]*len(flights) for _ in range(n+1)]

        dist[src][0]=0
        heap=[(0,src,-1)] # cost,node,#stop
        while heap:
            cost,node,n_stop = heapq.heappop(heap)
            if cost>dist[node][n_stop]:
                continue
            new_n_stop = n_stop+1
            if new_n_stop>k:
                continue
            for neighbor,c in graph[node]:
                new_cost =cost+c
                if new_cost<dist[neighbor][new_n_stop]:
                    heapq.heappush(heap,(new_cost,neighbor,new_n_stop))
                    dist[neighbor][new_n_stop]=new_cost
        cost = min(dist[dst])
        if cost ==float('inf'):
            return -1
        else: return cost