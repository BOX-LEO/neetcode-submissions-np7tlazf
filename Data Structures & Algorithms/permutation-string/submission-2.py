class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2 = len(s1),len(s2)
        if l1>l2:
            return False
        s1_dic = defaultdict(int)
        for i in s1:
            s1_dic[i]+=1
        
        l,r = 0,l1-1
        cur_dic = defaultdict(int)
        for i in s2[:r]:
            cur_dic[i]+=1
        while r<l2:
            cur_dic[s2[r]]+=1
            if cur_dic ==s1_dic:
                return True
            cur_dic[s2[l]]-=1
            if cur_dic[s2[l]]==0:
                del cur_dic[s2[l]]
            l+=1
            r+=1
        return False
            
