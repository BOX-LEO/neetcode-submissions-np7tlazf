class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val,self.min_list[-1])
        self.min_list.append(min_val)
        

    def pop(self) -> None:
        self.min_list.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()