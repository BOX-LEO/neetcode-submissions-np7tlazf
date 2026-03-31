class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        links = [[] for _ in range(n)]
        for s,r,time in times:
            links[s-1].append((r-1,time))      
        receive_time = [float('inf')]*n
        receive_time[k-1]=0
        heap = []
        heapq.heappush(heap,(0,k-1))
        while heap:
            time, source = heapq.heappop(heap)
            if time >receive_time[source]:
                continue
            
            for target, t in links[source]:
                new_time = receive_time[source]+t
                if receive_time[target]>new_time:
                    receive_time[target] = new_time
                    heapq.heappush(heap,(new_time,target))
        output = max(receive_time)
        if output == float('inf'):
            return -1
        else:
            return output