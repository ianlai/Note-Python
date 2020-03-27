from collections import deque 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        if not self.q2 or x <= self.q2[-1]:
            self.q2.append(x)

    def pop(self) -> None:
        last = self.q1.pop()
        if self.q2 and last == self.q2[-1]:
            self.q2.pop()

    def top(self) -> int:
        if self.q1:
            return self.q1[-1]

    def getMin(self) -> int:
        if self.q2:
            return self.q2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()