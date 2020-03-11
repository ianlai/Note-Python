# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.cur is not None:
            self.stack.append(self.cur)  #add cur when calling 
            self.cur = self.cur.left 
        next_node = self.stack.pop()
        self.cur = next_node.right       #let self.cur to 
        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.cur is None and len(self.stack) == 0:  #condition is AND because self.cur might point to None during the process
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()