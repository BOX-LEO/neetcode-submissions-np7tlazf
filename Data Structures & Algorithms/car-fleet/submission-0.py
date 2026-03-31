class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position,speed):
            cars.append((p,s))
        cars.sort(reverse=True)
        time=[(target-p)/s for p,s in cars]
        fleet = 1
        t = time.pop(0)
        while len(time)>0:
            t1 = time.pop(0)
            if t1>t:
                fleet+=1
                t = t1
        return fleet