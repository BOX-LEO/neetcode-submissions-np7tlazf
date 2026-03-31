class Solution:

    def isValid(self, s: str) -> bool:
        sl = [i for i in s]
        stack = []
        for i in sl:
            if i in ['(','[','{']:
                stack.append(i)
            elif i == ')':
                if len(stack)==0:
                    return False
                if stack.pop()!='(':
                    return False
            elif i ==']':
                if len(stack)==0:
                    return False
                if stack.pop()!='[':
                    return False
            elif i =='}':
                if len(stack)==0:
                    return False
                if stack.pop()!='{':
                    return False
        
        return stack ==[]
                    
        