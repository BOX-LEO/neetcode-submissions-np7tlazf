class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        clist = [i for i in s]
        cset = set(clist)
        if len(cset)<=1:
            return len(cset)
        maxl=1
        
        for i,c in enumerate(clist):
            l=1
            while l<=len(cset):
                # print(clist[i:i+l])
                if len(set(clist[i:i+l]))==l:
                    if l>maxl:
                        maxl=l
                    l+=1
                else:
                    break
        return maxl