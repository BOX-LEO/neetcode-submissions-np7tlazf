class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        l_max = 0
        for i in range(n):
            left[i]=l_max
            l_max = max(l_max,height[i])
        r_max = 0
        for i in range(n-1,-1,-1):
            right[i]=r_max
            r_max = max(r_max,height[i])
        res = 0
        for i in range(n):
            water = min(left[i],right[i])-height[i]
            if water>0:
                res+=water
        return res