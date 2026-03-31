class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[]
        t_list = []
        for i in s:
            s_list.append(i)
        for i in t:
            t_list.append(i)
        
        print(s_list)
        print(t_list)

        s_list.sort()
        t_list.sort()
        return s_list==t_list
        