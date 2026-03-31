class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        links = defaultdict(dict)
        for s,r,time in times:
            links[s][r]=time        
        receive_time = [float('inf')]*n
        receive_time[k-1]=0
        heap = []
        heapq.heappush(heap,(0,k))
        while heap:
            time, source = heapq.heappop(heap)
            if time >receive_time[source-1]:
                continue
            
            for target in links[source].keys():
                new_time = receive_time[source-1]+links[source][target]
                if receive_time[target-1]>new_time:
                    receive_time[target-1] = new_time
                    heapq.heappush(heap,(new_time,target))
        output = max(receive_time)
        if output == float('inf'):
            return -1
        else:
            return output