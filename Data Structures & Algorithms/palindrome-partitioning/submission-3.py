class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(string):
            length = len(string)
            if length==1:
                return True
            l,r = 0,length-1
            while l<=r:
                if string[l]==string[r]:
                    l+=1
                    r-=1
                else:return False
            return True
        
        res = []
        length = len(s)
        def backtrack(cur,index):
            if index == length:
                res.append(cur.copy())
                return
            temp = ''
            for i,c in enumerate(s[index:]):
                temp = temp+c
                print(temp)
                if ispalindrome(temp):
                    cur.append(temp)
                    backtrack(cur,index+i+1)
                    cur.pop()
        backtrack([],0)
        return res