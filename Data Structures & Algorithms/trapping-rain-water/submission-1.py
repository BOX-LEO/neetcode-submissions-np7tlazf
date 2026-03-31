class Solution:
    def trap(self, height: List[int]) -> int:
        
        load = 0
        l,r = 0,0
        while l<len(height):
            if height[l]==0:
                l+=1
                r+=1
            else:
                r+=1
                if r<len(height):
                    if height[r]>=height[l]:
                        for i in range(l+1,r):
                            load+=height[l]-height[i]
                        l=r
                    elif r==len(height)-1:
                        height[l] = max(height[l+1:])
                        r=l
                else:
                    l+=1
                    r=l

        return load
        