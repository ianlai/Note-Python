# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        q = collections.deque([root])
        ans = []
        layerSeq = 1 
        
        while q:
            layer = []
            for i in range(len(q)):      #extract until q is empty
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                layer.append(node.val)
                
            if layerSeq %2 == 1:
                ans.append(layer)
            else:
                ans.append(layer[::-1])
            layerSeq += 1
        return ans