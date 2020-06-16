# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Index the node from the leaves, so it's a bottom-up approach (From Discuss) [O(n), 81%]
    def findLeaves(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return -1
        #print(root.val, res)
        height = max(self.dfs(root.left, res), self.dfs(root.right, res)) + 1
        if height >= len(res):
            res.append([])
        res[height].append(root.val)
        return height

    # =========================================
    
    # Recursively pre-order traverse; collect and remove the leaves; start over until no nodes [O(n2), 57%]
    def findLeaves1(self, root: TreeNode) -> List[List[int]]:
        print("Pre-order traverse")
        if not root:
            return []
        
        ans = []
        while root.left or root.right: 
            cur = []
            self.collectLeaves(None, root, cur)
            ans.append(cur)
            #print(ans)
        ans.append([root.val])
        return ans

    def collectLeaves(self, parent, node, cur):
        if not node:
            print("NONE")
            return 

        if not node.left and not node.right:
            cur.append(node.val)
            if not parent:
                return 
            if id(parent.left) == id(node):
                parent.left = None
            else:
                parent.right = None
            return
        
        self.collectLeaves(node, node.left, cur)
        self.collectLeaves(node, node.right, cur)
            
        