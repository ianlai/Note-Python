# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Traversal [space: O(n), time: O(n), 54%]
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodelist = []
        self.traverse(root, nodelist)
        
        count = collections.Counter(nodelist)
        mostCount = 0
        mostElemnt = -1
        ans = []
        for k in count:
            mostCount = max(mostCount, count[k])
        for k in count:
            if count[k] == mostCount:
                ans.append(k)
        return ans
    
    def traverse(self, root, nodelist):
        if not root:
            return 
        
        self.traverse(root.left, nodelist)
        nodelist.append(root.val)
        self.traverse(root.right, nodelist)
        return 
        
        
        
        