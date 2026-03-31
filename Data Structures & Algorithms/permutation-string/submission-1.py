class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        if l1 > len(s2):
            return False

        s1_list = [i for i in s1]
        s1_list.sort()
        print(s1_list)

        for l in range(len(s2)-l1+1):
            if set(s1) == set(s2[l:l+l1]):
                sub = [i for i in s2[l:l+l1]]
                sub.sort()
                print(sub)
                if s1_list == sub:
                    return True
                
            

        return False