class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stack = []
        for t in tokens:
            if t in operators:
                l2 = stack.pop()
                l1 = stack.pop()
                if t =='+':
                    stack.append(l1+l2)
                elif t =='-':
                    stack.append(l1-l2)
                elif t == '*':
                    stack.append(l1*l2)
                else:
                    stack.append(int(l1/l2))
            else:
                stack.append(int(t))
        return stack[0]