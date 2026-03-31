class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers=[]
        operators ={'+','-','*','/'}
        for t in tokens:
            if t not in operators:
                numbers.append(int(t))
            elif t == '+':
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(a+b)
            elif t =='-':
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(b-a)
            elif t=='*':
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(a*b)
            elif t=='/':
                a = numbers.pop()
                b = numbers.pop()
                print(a,b)
                numbers.append(int(b/a))
        return numbers[0]