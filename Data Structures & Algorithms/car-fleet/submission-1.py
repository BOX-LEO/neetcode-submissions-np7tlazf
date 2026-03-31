class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dis_time = [[target-p,(target-p)/s] for p, s in zip(position, speed)]
        dis_time.sort(key = lambda x:x[0])
        res = 0
        time = 0
        for d,t in dis_time:
            if t>time:
                res+=1
                time = t
        return res