from collections import deque

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(0)
n1   = TreeNode(1)
n2   = TreeNode(2)
n3   = TreeNode(3)
n4   = TreeNode(4)
n5   = TreeNode(5)
root.left  = n1 
root.right = n2
n1.left    = n3
n1.right   = n4
n2.left    = n5

class Solution():
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return [] 
        
        queue = [root]   #list 
        result = []
        while queue:
            next_queue = []

            # add the values of the current layer into result (general)
            # layer = []
            # for cur in queue: 
            #     layer.append(cur.val)
            # result.append(layer)

            # add the values of the current layer into result (python)
            result.append([node.val for node in queue])
 
            # add the left and right of the current layer into next_queue
            for cur in queue: 
                if cur.left:
                    next_queue.append(cur.left)
                if cur.right:
                    next_queue.append(cur.right)

            queue = next_queue
        return result

    def levelOrderWithoutLevelInfo(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([root])  #deque
        result = []
        while len(queue) > 0 : 
            cur = queue.popleft()
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result

sol = Solution()
print(sol.levelOrderWithoutLevelInfo(root))
print(sol.levelOrder(root))
