# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        self.dfs2(root, ans, [], sum)
        return ans
    
    # End at the last layer
    def dfs(self, node, ans, arr, sum):
        # End condition
        if not node.left and not node.right:
            #print(arr, "sum = ", sum)
            if sum == node.val:
                arr.append(node.val)
                ans.append(arr)
            return 
        #print(node.val)
        # Go left
        if node.left:
            self.dfs(node.left, ans, arr+[node.val], sum-node.val)
            
        # Go right
        if node.right:
            self.dfs(node.right, ans, arr+[node.val], sum-node.val)
        return

    # End at the leaf layer
    def dfs2(self, node, ans, arr, sum):
        # End condition
        if not node:
            if sum == 0:
                ans.append(arr)
            return 
        # Go right
        if not node.left:
            self.dfs2(node.right, ans, arr+[node.val], sum-node.val)
        # Go left
        elif not node.right:
            self.dfs2(node.left, ans, arr+[node.val], sum-node.val)
        # Go both 
        elif node.left and node.right:
            self.dfs2(node.right, ans, arr+[node.val], sum-node.val)
            self.dfs2(node.left, ans, arr+[node.val], sum-node.val)
        return 