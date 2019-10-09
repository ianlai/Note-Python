# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive: speed only 5% 
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        
        max_value = max(nums)
        max_index = nums.index(max_value)
        root = TreeNode(max_value)
        root.left  = self.helper(nums, 0, max_index-1, root)
        root.right = self.helper(nums, max_index + 1, len(nums) - 1, root)
        return root
        
    def helper(self, nums, start, end, parent):
        #print(nums, "s=", start, "e=", end)
        if nums is None:
            return None
        if start > end:
            return None
        
        subnums = nums[start:end+1]
        max_value = max(subnums)
        max_index = nums.index(max_value)
        #print(nums, "s=", start, "e=", end, "max=", max_value, "index=", max_index)
        node = TreeNode(max_value)
        node.left  = self.helper(nums, start, max_index-1, node)
        node.right = self.helper(nums, max_index+1, end, node)
        
        return node
        
        
        