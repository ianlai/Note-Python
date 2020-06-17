# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS with sorting [O(N + WlogW + WHlogH), 80%]
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        ans = []
        
        idxToVal = collections.defaultdict(list)
        self.helper(root, idxToVal, 0, 0)
        
        for key in sorted(idxToVal):
            verts = sorted(idxToVal[key], key = lambda x:x[0])  # IMPORTANT: need to specify the key
                                                                # Without the key, it will sort by x[0] first than x[1] (maybe)
                                                                # However, we want to sort by x[0] but keep others in insertion order
            tmp = []
            for node in verts:
                tmp.append(node[1])

            ans.append(tmp)
        return ans
            
    def helper(self, node, idxToVal, idx, layer):
        if not node:
            return
        
        # Pre-order DFS
        idxToVal[idx].append([layer, node.val])
        self.helper(node.left, idxToVal, idx - 1, layer + 1)
        self.helper(node.right, idxToVal, idx + 1, layer + 1)
        