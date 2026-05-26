class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        l1,l2 = len(s1),len(s2)
        for i in range(l2-l1+1):
            temp_count = Counter(s2[i:i+l1])
            if temp_count == s1_count:
                return True
        return False