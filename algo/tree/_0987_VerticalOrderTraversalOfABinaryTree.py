# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Set the coordinate (x, layer) for each node, sort based on x, layer, value [O(nlogn)?? , 35%]
    # Two layer sorting 
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        idxToNodes = {}
        
        self.helper(root, 0, 0, idxToNodes)
        idxToNodes_sorted = sorted(idxToNodes.items(), key=lambda x:x[0])
        for e in idxToNodes_sorted:
            #print(e)
            ans.append([])
            for t in sorted(e[1], key=lambda x:(x[0], x[1])):    
                #print("  ", t)
                ans[-1].append(t[1])
        return ans
        
    def helper(self, root, idx, layer, idxToNodes):
        if not root:
            return 
        
        if idx in idxToNodes:
            idxToNodes[idx].append((layer, root.val))
        else:
            idxToNodes[idx] = []
            idxToNodes[idx].append((layer, root.val))
        
        self.helper(root.left,  idx-1, layer+1, idxToNodes)
        self.helper(root.right, idx+1, layer+1, idxToNodes)