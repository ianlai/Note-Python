class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = 0
        self.cap = size
        self.deque = collections.deque([])

    def next(self, val: int) -> float:
        if len(self.deque) == self.cap:
            left = self.deque[0]
            self.deque.popleft()
            self.deque.append(val)
            self.sum = self.sum - left + val
        else:
            self.deque.append(val)
            self.sum = self.sum + val
        return self.sum / len(self.deque)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)