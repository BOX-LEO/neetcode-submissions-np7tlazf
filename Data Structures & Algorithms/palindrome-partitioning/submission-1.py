class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def is_Palindrome(s:str):
            if len(s)<1:
                return False
            left,right = 0,len(s)-1
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:return False
            return True
        


        def subset(res:list,rem:str):
            if rem=="":
                result.append(res.copy())

            else:
                for i in range(len(rem)+1):
                    if is_Palindrome(rem[:i]):
                        res.append(rem[:i])
                        subset(res,rem[i:])
                        res.pop()

        subset([],s)
        return result