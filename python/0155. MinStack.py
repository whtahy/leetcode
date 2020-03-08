class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            self.min.append(min(x, self.min[-1]))
        else:
            self.min.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
