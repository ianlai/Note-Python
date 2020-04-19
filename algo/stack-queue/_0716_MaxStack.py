class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p1 = []
        self.p2 = []
        
    def push(self, x: int) -> None:
        self.p1.append(x)
        if not self.p2 or x >= self.p2[-1]:
            self.p2.append(x)

    def pop(self) -> int:
        x = self.p1.pop()
        if self.p2 and x == self.p2[-1]:
            self.p2.pop()
        return x

    def top(self) -> int:
        if self.p1:
            return self.p1[-1]
        return -1

    def peekMax(self) -> int:
        if self.p2:
            return self.p2[-1]
        else:
            return self.p1[-1]
        
    # No. 155 Min Stack doesn't have this function. 
    # It's more complex if we allow the user to pop the max 
    # (1) Remove the max in p2 if it's there 
    # (2) Find the max in p1
    # (3) Move the elements after the max in p1 into a temp stack
    # (4) Remove the max in p1
    # (5) Add the temp stack back to p1 
    def popMax(self) -> int:
        x = 0 
        if self.p2:
            x = self.p2.pop()
        elif self.p1: #p2 is empty  
            x = max(self.p1)
        #self.p1.remove(x)  #find the first match 
        temp = []
        for i in range(len(self.p1)-1, -1, -1):  #find the last match
            if self.p1[i] != x:
                temp.append(self.p1.pop())
            else:
                self.p1.pop(i)
                while temp:
                    self.push(temp.pop())  #temp is also a stack
                break
        #print(self.p1, self.p2, temp)
        return x

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()