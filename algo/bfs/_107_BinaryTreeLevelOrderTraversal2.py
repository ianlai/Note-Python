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

    # (1) Use a deque to achieve popleft to avoid using two list.
    # (2) Though the queue's size seems to vary during iteration, 
    #     range() fixes the size in the beginning.
    # (3) Reverse the output list in the end. 
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []
        while queue:
            layer = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                layer.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(layer)
        return result[::-1]

sol = Solution()
print(sol.levelOrderBottom(root))