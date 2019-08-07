from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque([]) #main 
        self.q2 = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        self.topElement = x 
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            
            # popleft and append to q2 until left 1
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
                
            # the left 1 should be returned and removed 
            popElement = self.q1.pop()
            
            # popleft q2 back to q1; update the topElement one by one
            while len(self.q2) > 0:
                self.topElement = self.q2.popleft()
                self.q1.append(self.topElement)
                
            return popElement
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topElement  #assume calling top only after push is called

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.q1 or self.q2:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()