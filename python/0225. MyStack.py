# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# nested queues
class MyStack:
    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        front = deque([x])
        front.append(self.dq)
        self.dq = front

    def pop(self) -> int:
        x = self.dq.popleft()
        self.dq = self.dq[0]
        return x

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0

# rotate queue
class MyStack:
    def __init__(self):
        self.dq = deque() # append(), popleft()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        # self.dq.rotate(-1)
        for _ in range(len(self.dq) - 1):
            self.dq.append(self.dq.popleft())
        return self.dq.popleft()

    def top(self) -> int:
        x = self.pop()
        self.dq.append(x)
        return x

    def empty(self) -> bool:
        return len(self.dq) == 0

# 2 queues
class MyStack:
    def __init__(self):
        self.dq = deque()
        self.tmp = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        while len(self.dq) > 1:
            self.tmp.append(self.dq.popleft())
        self.dq, self.tmp = self.tmp, self.dq
        return self.tmp.popleft()

    def top(self) -> int:
        x = self.pop()
        self.dq.append(x)
        return x

    def empty(self) -> bool:
        return len(self.dq) == 0
