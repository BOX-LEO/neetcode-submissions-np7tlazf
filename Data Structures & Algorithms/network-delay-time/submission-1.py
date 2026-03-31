class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        links = defaultdict(dict)
        for s,r,time in times:
            links[s][r]=time        
        received = set()
        received.add(k)
        res = [float('inf')]*n
        def backtrack(cur,time,seen):
            seen.add(cur)
            res[cur-1] = min(res[cur-1],time)
            for k in links[cur].keys():
                if k not in seen:
                    backtrack(k,res[cur-1]+links[cur][k],seen)
            seen.remove(cur)

        backtrack(k,0,set())
        output = max(res)
        if output == float('inf'):
            return -1
        return output


