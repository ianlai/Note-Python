# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Goal: Find the nodes with the most occurrence 
    # e.g. [1,1,1,1,2,2,3,3,3,3,4,4] -> [1,3]
    
    # Traversal1 with no list (use global var) 
    # In-order DFS + BST = ascending list 
    # We can compare the i node and i-1 node while traversing to find the duplication 
    #
    # [space: O(1) with stack, time: O(n), 76%]
    
    prev = None 
    count, maxCount = 0, 0
    nodelist = []
    
    def findMode(self, root: TreeNode) -> List[int]:
        print("Traversal with no list [space:O(1) despite of stack]")
        if not root:
            return []
        self.traverse(root)
        return self.nodelist

    def traverse(self, node):
        if not node:
            return 
        
        # 1. Go left
        self.traverse(node.left)
        
        # 2. When traverse to current node (start)
        if self.prev == node.val:
            self.count += 1 
        else:
            self.count = 1
        
        if self.count == self.maxCount:
            self.nodelist.append(node.val)
        elif self.count > self.maxCount:
            self.nodelist = [node.val] #clear and add the current one
            self.maxCount = self.count
            
        self.prev = node.val
        
        # 3. Go right
        self.traverse(node.right)
        
    # =============================================
    
    # NOT fitting the requirement of constant space!  
    #
    # Traverse and use counter to find the elements with the most occurence 
    # [space: O(n), time: O(n), 54%]
    
    def findMode2(self, root: TreeNode) -> List[int]:
        print("Traversal with list [space:O(n)]")
        if not root:
            return []
        nodelist = []
        self.traverse2(root, nodelist)
        
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
    
    def traverse2(self, root, nodelist):
        if not root:
            return 
        
        self.traverse2(root.left, nodelist)
        nodelist.append(root.val)
        self.traverse2(root.right, nodelist)
        return 