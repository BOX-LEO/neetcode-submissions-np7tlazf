class MinStack:

    def __init__(self):
        self.stack = [float('inf')]
        self.minstack = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.minstack[-1]:
            min_val = val
        else:
            min_val = self.minstack[-1]
        self.minstack.append(min_val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
